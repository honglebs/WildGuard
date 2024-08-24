import { n as noop, c as create_ssr_component, a as subscribe, e as escape, b as add_attribute, v as validate_component } from "../../chunks/ssr.js";
import { w as writable } from "../../chunks/index2.js";
const is_client = typeof window !== "undefined";
let now = is_client ? () => window.performance.now() : () => Date.now();
let raf = is_client ? (cb) => requestAnimationFrame(cb) : noop;
const tasks = /* @__PURE__ */ new Set();
function run_tasks(now2) {
  tasks.forEach((task) => {
    if (!task.c(now2)) {
      tasks.delete(task);
      task.f();
    }
  });
  if (tasks.size !== 0) raf(run_tasks);
}
function loop(callback) {
  let task;
  if (tasks.size === 0) raf(run_tasks);
  return {
    promise: new Promise((fulfill) => {
      tasks.add(task = { c: callback, f: fulfill });
    }),
    abort() {
      tasks.delete(task);
    }
  };
}
function is_date(obj) {
  return Object.prototype.toString.call(obj) === "[object Date]";
}
function tick_spring(ctx, last_value, current_value, target_value) {
  if (typeof current_value === "number" || is_date(current_value)) {
    const delta = target_value - current_value;
    const velocity = (current_value - last_value) / (ctx.dt || 1 / 60);
    const spring2 = ctx.opts.stiffness * delta;
    const damper = ctx.opts.damping * velocity;
    const acceleration = (spring2 - damper) * ctx.inv_mass;
    const d = (velocity + acceleration) * ctx.dt;
    if (Math.abs(d) < ctx.opts.precision && Math.abs(delta) < ctx.opts.precision) {
      return target_value;
    } else {
      ctx.settled = false;
      return is_date(current_value) ? new Date(current_value.getTime() + d) : current_value + d;
    }
  } else if (Array.isArray(current_value)) {
    return current_value.map(
      (_, i) => tick_spring(ctx, last_value[i], current_value[i], target_value[i])
    );
  } else if (typeof current_value === "object") {
    const next_value = {};
    for (const k in current_value) {
      next_value[k] = tick_spring(ctx, last_value[k], current_value[k], target_value[k]);
    }
    return next_value;
  } else {
    throw new Error(`Cannot spring ${typeof current_value} values`);
  }
}
function spring(value, opts = {}) {
  const store = writable(value);
  const { stiffness = 0.15, damping = 0.8, precision = 0.01 } = opts;
  let last_time;
  let task;
  let current_token;
  let last_value = value;
  let target_value = value;
  let inv_mass = 1;
  let inv_mass_recovery_rate = 0;
  let cancel_task = false;
  function set(new_value, opts2 = {}) {
    target_value = new_value;
    const token = current_token = {};
    if (value == null || opts2.hard || spring2.stiffness >= 1 && spring2.damping >= 1) {
      cancel_task = true;
      last_time = now();
      last_value = new_value;
      store.set(value = target_value);
      return Promise.resolve();
    } else if (opts2.soft) {
      const rate = opts2.soft === true ? 0.5 : +opts2.soft;
      inv_mass_recovery_rate = 1 / (rate * 60);
      inv_mass = 0;
    }
    if (!task) {
      last_time = now();
      cancel_task = false;
      task = loop((now2) => {
        if (cancel_task) {
          cancel_task = false;
          task = null;
          return false;
        }
        inv_mass = Math.min(inv_mass + inv_mass_recovery_rate, 1);
        const ctx = {
          inv_mass,
          opts: spring2,
          settled: true,
          dt: (now2 - last_time) * 60 / 1e3
        };
        const next_value = tick_spring(ctx, last_value, value, target_value);
        last_time = now2;
        last_value = value;
        store.set(value = next_value);
        if (ctx.settled) {
          task = null;
        }
        return !ctx.settled;
      });
    }
    return new Promise((fulfil) => {
      task.promise.then(() => {
        if (token === current_token) fulfil();
      });
    });
  }
  const spring2 = {
    set,
    update: (fn, opts2) => set(fn(target_value, value), opts2),
    subscribe: store.subscribe,
    stiffness,
    damping,
    precision
  };
  return spring2;
}
const css$1 = {
  code: ".counter.svelte-y96mxt.svelte-y96mxt{display:flex;border-top:1px solid rgba(0, 0, 0, 0.1);border-bottom:1px solid rgba(0, 0, 0, 0.1);margin:1rem 0}.counter.svelte-y96mxt button.svelte-y96mxt{width:2em;padding:0;display:flex;align-items:center;justify-content:center;border:0;background-color:transparent;touch-action:manipulation;font-size:2rem}.counter.svelte-y96mxt button.svelte-y96mxt:hover{background-color:var(--color-bg-1)}svg.svelte-y96mxt.svelte-y96mxt{width:25%;height:25%}path.svelte-y96mxt.svelte-y96mxt{vector-effect:non-scaling-stroke;stroke-width:2px;stroke:#444}.counter-viewport.svelte-y96mxt.svelte-y96mxt{width:8em;height:4em;overflow:hidden;text-align:center;position:relative}.counter-viewport.svelte-y96mxt strong.svelte-y96mxt{position:absolute;display:flex;width:100%;height:100%;font-weight:400;color:var(--color-theme-1);font-size:4rem;align-items:center;justify-content:center}.counter-digits.svelte-y96mxt.svelte-y96mxt{position:absolute;width:100%;height:100%}.hidden.svelte-y96mxt.svelte-y96mxt{top:-100%;user-select:none}",
  map: `{"version":3,"file":"Counter.svelte","sources":["Counter.svelte"],"sourcesContent":["<script>\\n\\timport { spring } from 'svelte/motion';\\n\\n\\tlet count = 0;\\n\\n\\tconst displayed_count = spring();\\n\\t$: displayed_count.set(count);\\n\\t$: offset = modulo($displayed_count, 1);\\n\\n\\t/**\\n\\t * @param {number} n\\n\\t * @param {number} m\\n\\t */\\n\\tfunction modulo(n, m) {\\n\\t\\t// handle negative numbers\\n\\t\\treturn ((n % m) + m) % m;\\n\\t}\\n<\/script>\\n\\n<div class=\\"counter\\">\\n\\t<button on:click={() => (count -= 1)} aria-label=\\"Decrease the counter by one\\">\\n\\t\\t<svg aria-hidden=\\"true\\" viewBox=\\"0 0 1 1\\">\\n\\t\\t\\t<path d=\\"M0,0.5 L1,0.5\\" />\\n\\t\\t</svg>\\n\\t</button>\\n\\n\\t<div class=\\"counter-viewport\\">\\n\\t\\t<div class=\\"counter-digits\\" style=\\"transform: translate(0, {100 * offset}%)\\">\\n\\t\\t\\t<strong class=\\"hidden\\" aria-hidden=\\"true\\">{Math.floor($displayed_count + 1)}</strong>\\n\\t\\t\\t<strong>{Math.floor($displayed_count)}</strong>\\n\\t\\t</div>\\n\\t</div>\\n\\n\\t<button on:click={() => (count += 1)} aria-label=\\"Increase the counter by one\\">\\n\\t\\t<svg aria-hidden=\\"true\\" viewBox=\\"0 0 1 1\\">\\n\\t\\t\\t<path d=\\"M0,0.5 L1,0.5 M0.5,0 L0.5,1\\" />\\n\\t\\t</svg>\\n\\t</button>\\n</div>\\n\\n<style>\\n\\t.counter {\\n\\t\\tdisplay: flex;\\n\\t\\tborder-top: 1px solid rgba(0, 0, 0, 0.1);\\n\\t\\tborder-bottom: 1px solid rgba(0, 0, 0, 0.1);\\n\\t\\tmargin: 1rem 0;\\n\\t}\\n\\n\\t.counter button {\\n\\t\\twidth: 2em;\\n\\t\\tpadding: 0;\\n\\t\\tdisplay: flex;\\n\\t\\talign-items: center;\\n\\t\\tjustify-content: center;\\n\\t\\tborder: 0;\\n\\t\\tbackground-color: transparent;\\n\\t\\ttouch-action: manipulation;\\n\\t\\tfont-size: 2rem;\\n\\t}\\n\\n\\t.counter button:hover {\\n\\t\\tbackground-color: var(--color-bg-1);\\n\\t}\\n\\n\\tsvg {\\n\\t\\twidth: 25%;\\n\\t\\theight: 25%;\\n\\t}\\n\\n\\tpath {\\n\\t\\tvector-effect: non-scaling-stroke;\\n\\t\\tstroke-width: 2px;\\n\\t\\tstroke: #444;\\n\\t}\\n\\n\\t.counter-viewport {\\n\\t\\twidth: 8em;\\n\\t\\theight: 4em;\\n\\t\\toverflow: hidden;\\n\\t\\ttext-align: center;\\n\\t\\tposition: relative;\\n\\t}\\n\\n\\t.counter-viewport strong {\\n\\t\\tposition: absolute;\\n\\t\\tdisplay: flex;\\n\\t\\twidth: 100%;\\n\\t\\theight: 100%;\\n\\t\\tfont-weight: 400;\\n\\t\\tcolor: var(--color-theme-1);\\n\\t\\tfont-size: 4rem;\\n\\t\\talign-items: center;\\n\\t\\tjustify-content: center;\\n\\t}\\n\\n\\t.counter-digits {\\n\\t\\tposition: absolute;\\n\\t\\twidth: 100%;\\n\\t\\theight: 100%;\\n\\t}\\n\\n\\t.hidden {\\n\\t\\ttop: -100%;\\n\\t\\tuser-select: none;\\n\\t}\\n</style>\\n"],"names":[],"mappings":"AAyCC,oCAAS,CACR,OAAO,CAAE,IAAI,CACb,UAAU,CAAE,GAAG,CAAC,KAAK,CAAC,KAAK,CAAC,CAAC,CAAC,CAAC,CAAC,CAAC,CAAC,CAAC,CAAC,GAAG,CAAC,CACxC,aAAa,CAAE,GAAG,CAAC,KAAK,CAAC,KAAK,CAAC,CAAC,CAAC,CAAC,CAAC,CAAC,CAAC,CAAC,CAAC,GAAG,CAAC,CAC3C,MAAM,CAAE,IAAI,CAAC,CACd,CAEA,sBAAQ,CAAC,oBAAO,CACf,KAAK,CAAE,GAAG,CACV,OAAO,CAAE,CAAC,CACV,OAAO,CAAE,IAAI,CACb,WAAW,CAAE,MAAM,CACnB,eAAe,CAAE,MAAM,CACvB,MAAM,CAAE,CAAC,CACT,gBAAgB,CAAE,WAAW,CAC7B,YAAY,CAAE,YAAY,CAC1B,SAAS,CAAE,IACZ,CAEA,sBAAQ,CAAC,oBAAM,MAAO,CACrB,gBAAgB,CAAE,IAAI,YAAY,CACnC,CAEA,+BAAI,CACH,KAAK,CAAE,GAAG,CACV,MAAM,CAAE,GACT,CAEA,gCAAK,CACJ,aAAa,CAAE,kBAAkB,CACjC,YAAY,CAAE,GAAG,CACjB,MAAM,CAAE,IACT,CAEA,6CAAkB,CACjB,KAAK,CAAE,GAAG,CACV,MAAM,CAAE,GAAG,CACX,QAAQ,CAAE,MAAM,CAChB,UAAU,CAAE,MAAM,CAClB,QAAQ,CAAE,QACX,CAEA,+BAAiB,CAAC,oBAAO,CACxB,QAAQ,CAAE,QAAQ,CAClB,OAAO,CAAE,IAAI,CACb,KAAK,CAAE,IAAI,CACX,MAAM,CAAE,IAAI,CACZ,WAAW,CAAE,GAAG,CAChB,KAAK,CAAE,IAAI,eAAe,CAAC,CAC3B,SAAS,CAAE,IAAI,CACf,WAAW,CAAE,MAAM,CACnB,eAAe,CAAE,MAClB,CAEA,2CAAgB,CACf,QAAQ,CAAE,QAAQ,CAClB,KAAK,CAAE,IAAI,CACX,MAAM,CAAE,IACT,CAEA,mCAAQ,CACP,GAAG,CAAE,KAAK,CACV,WAAW,CAAE,IACd"}`
};
function modulo(n, m) {
  return (n % m + m) % m;
}
const Counter = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let offset;
  let $displayed_count, $$unsubscribe_displayed_count;
  let count = 0;
  const displayed_count = spring();
  $$unsubscribe_displayed_count = subscribe(displayed_count, (value) => $displayed_count = value);
  $$result.css.add(css$1);
  {
    displayed_count.set(count);
  }
  offset = modulo($displayed_count, 1);
  $$unsubscribe_displayed_count();
  return `<div class="counter svelte-y96mxt"><button aria-label="Decrease the counter by one" class="svelte-y96mxt" data-svelte-h="svelte-97ppyc"><svg aria-hidden="true" viewBox="0 0 1 1" class="svelte-y96mxt"><path d="M0,0.5 L1,0.5" class="svelte-y96mxt"></path></svg></button> <div class="counter-viewport svelte-y96mxt"><div class="counter-digits svelte-y96mxt" style="${"transform: translate(0, " + escape(100 * offset, true) + "%)"}"><strong class="hidden svelte-y96mxt" aria-hidden="true">${escape(Math.floor($displayed_count + 1))}</strong> <strong class="svelte-y96mxt">${escape(Math.floor($displayed_count))}</strong></div></div> <button aria-label="Increase the counter by one" class="svelte-y96mxt" data-svelte-h="svelte-irev0c"><svg aria-hidden="true" viewBox="0 0 1 1" class="svelte-y96mxt"><path d="M0,0.5 L1,0.5 M0.5,0 L0.5,1" class="svelte-y96mxt"></path></svg></button> </div>`;
});
const welcome = "/_app/immutable/assets/svelte-welcome.0pIiHnVF.webp";
const welcome_fallback = "/_app/immutable/assets/svelte-welcome.VNiyy3gC.png";
const css = {
  code: "section.svelte-19xx0bt.svelte-19xx0bt{display:flex;flex-direction:column;justify-content:center;align-items:center;flex:0.6}h1.svelte-19xx0bt.svelte-19xx0bt{width:100%}.welcome.svelte-19xx0bt.svelte-19xx0bt{display:block;position:relative;width:100%;height:0;padding:0 0 calc(100% * 495 / 2048) 0}.welcome.svelte-19xx0bt img.svelte-19xx0bt{position:absolute;width:100%;height:100%;top:0;display:block}",
  map: `{"version":3,"file":"+page.svelte","sources":["+page.svelte"],"sourcesContent":["<script>\\n\\timport Counter from './Counter.svelte';\\n\\timport welcome from '$lib/images/svelte-welcome.webp';\\n\\timport welcome_fallback from '$lib/images/svelte-welcome.png';\\n<\/script>\\n\\n<svelte:head>\\n\\t<title>Home</title>\\n\\t<meta name=\\"description\\" content=\\"Svelte demo app\\" />\\n</svelte:head>\\n\\n<section>\\n\\t<h1>\\n\\t\\t<span class=\\"welcome\\">\\n\\t\\t\\t<picture>\\n\\t\\t\\t\\t<source srcset={welcome} type=\\"image/webp\\" />\\n\\t\\t\\t\\t<img src={welcome_fallback} alt=\\"Welcome\\" />\\n\\t\\t\\t</picture>\\n\\t\\t</span>\\n\\n\\t\\tto your new<br />SvelteKit app\\n\\t</h1>\\n\\n\\t<h2>\\n\\t\\ttry editing <strong>src/routes/+page.svelte</strong>\\n\\t</h2>\\n\\n\\t<Counter />\\n</section>\\n\\n<style>\\n\\tsection {\\n\\t\\tdisplay: flex;\\n\\t\\tflex-direction: column;\\n\\t\\tjustify-content: center;\\n\\t\\talign-items: center;\\n\\t\\tflex: 0.6;\\n\\t}\\n\\n\\th1 {\\n\\t\\twidth: 100%;\\n\\t}\\n\\n\\t.welcome {\\n\\t\\tdisplay: block;\\n\\t\\tposition: relative;\\n\\t\\twidth: 100%;\\n\\t\\theight: 0;\\n\\t\\tpadding: 0 0 calc(100% * 495 / 2048) 0;\\n\\t}\\n\\n\\t.welcome img {\\n\\t\\tposition: absolute;\\n\\t\\twidth: 100%;\\n\\t\\theight: 100%;\\n\\t\\ttop: 0;\\n\\t\\tdisplay: block;\\n\\t}\\n</style>\\n"],"names":[],"mappings":"AA+BC,qCAAQ,CACP,OAAO,CAAE,IAAI,CACb,cAAc,CAAE,MAAM,CACtB,eAAe,CAAE,MAAM,CACvB,WAAW,CAAE,MAAM,CACnB,IAAI,CAAE,GACP,CAEA,gCAAG,CACF,KAAK,CAAE,IACR,CAEA,sCAAS,CACR,OAAO,CAAE,KAAK,CACd,QAAQ,CAAE,QAAQ,CAClB,KAAK,CAAE,IAAI,CACX,MAAM,CAAE,CAAC,CACT,OAAO,CAAE,CAAC,CAAC,CAAC,CAAC,KAAK,IAAI,CAAC,CAAC,CAAC,GAAG,CAAC,CAAC,CAAC,IAAI,CAAC,CAAC,CACtC,CAEA,uBAAQ,CAAC,kBAAI,CACZ,QAAQ,CAAE,QAAQ,CAClB,KAAK,CAAE,IAAI,CACX,MAAM,CAAE,IAAI,CACZ,GAAG,CAAE,CAAC,CACN,OAAO,CAAE,KACV"}`
};
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  $$result.css.add(css);
  return `${$$result.head += `<!-- HEAD_svelte-t32ptj_START -->${$$result.title = `<title>Home</title>`, ""}<meta name="description" content="Svelte demo app"><!-- HEAD_svelte-t32ptj_END -->`, ""} <section class="svelte-19xx0bt"><h1 class="svelte-19xx0bt" data-svelte-h="svelte-11s73ib"><span class="welcome svelte-19xx0bt"><picture><source${add_attribute("srcset", welcome, 0)} type="image/webp"> <img${add_attribute("src", welcome_fallback, 0)} alt="Welcome" class="svelte-19xx0bt"></picture></span>

		to your new<br>SvelteKit app</h1> <h2 data-svelte-h="svelte-1e36z0s">try editing <strong>src/routes/+page.svelte</strong></h2> ${validate_component(Counter, "Counter").$$render($$result, {}, {}, {})} </section>`;
});
export {
  Page as default
};
