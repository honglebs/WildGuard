import * as universal from '../entries/pages/_page.js';

export const index = 2;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/_page.svelte.js')).default;
export { universal };
export const universal_id = "src/routes/+page.js";
export const imports = ["_app/immutable/nodes/2.QKAvpFF6.js","_app/immutable/chunks/scheduler.Dk-snqIU.js","_app/immutable/chunks/index.B-IpIKmi.js","_app/immutable/chunks/index.Ice1EKvx.js"];
export const stylesheets = ["_app/immutable/assets/2.Cs8KR-Bb.css"];
export const fonts = [];
