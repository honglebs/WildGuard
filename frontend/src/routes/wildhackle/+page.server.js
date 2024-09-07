import { fail } from '@sveltejs/kit';
import { Game } from './game';

/** @satisfies {import('./$types').PageServerLoad} */
export const load = ({ cookies }) => {
	const cookieValue = cookies.get('wildhackle') || '';
	const game = new Game(cookieValue);

	return {
		/**
		 * The player's guessed words so far
		 */
		guesses: game.guesses || [],

		/**
		 * An array of strings like '__x_c' corresponding to the guesses, where 'x' means
		 * an exact match, and 'c' means a close match (right letter, wrong place)
		 */
		answers: game.answers || [],

		/**
		 * The correct answer, revealed if the game is over
		 */
		answer: game.answers.length >= 6 ? game.answer : null
	};
};

/** @satisfies {import('./$types').Actions} */
export const actions = {
	/**
	 * Modify game state in reaction to a keypress. If client-side JavaScript
	 * is available, this will happen in the browser instead of here
	 */
	update: async ({ request, cookies }) => {
		try {
			const game = new Game(cookies.get('wildhackle') || '');

			const data = await request.formData();
			const key = data.get('key');

			const i = game.answers.length;

			if (key === 'backspace') {
				game.guesses[i] = game.guesses[i] ? game.guesses[i].slice(0, -1) : '';
			} else {
				game.guesses[i] = (game.guesses[i] || '') + key;
			}

			cookies.set('wildhackle', game.toString(), { path: '/' });
		} catch (error) {
			console.error('Update error:', error);
			return fail(500, { message: 'Internal server error during update' });
		}
	},

	/**
	 * Modify game state in reaction to a guessed word. This logic always runs on
	 * the server, so that people can't cheat by peeking at the JavaScript
	 */
	enter: async ({ request, cookies }) => {
		try {
			const game = new Game(cookies.get('wildhackle') || '');

			const data = await request.formData();
			const guess = /** @type {string[]} */ (data.getAll('guess'));

			if (!game.enter(guess)) {
				return fail(400, { badGuess: true });
			}

			cookies.set('wildhackle', game.toString(), { path: '/' });
		} catch (error) {
			console.error('Enter error:', error);
			return fail(500, { message: 'Internal server error during enter' });
		}
	},

	restart: async ({ cookies }) => {
		try {
			cookies.delete('wildhackle', { path: '/' });
		} catch (error) {
			console.error('Restart error:', error);
			return fail(500, { message: 'Internal server error during restart' });
		}
	}
};
