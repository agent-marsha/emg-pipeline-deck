import base64, pathlib

F = pathlib.Path("/root/signal-safari/_build/fonts")
b64 = {n: base64.b64encode((F / n).read_bytes()).decode() for n in ("baloo2.woff2", "nunito.woff2")}

CSS = """
@font-face{font-family:'Baloo 2';font-style:normal;font-weight:400 800;src:url(data:font/woff2;base64,__BALOO__) format('woff2')}
@font-face{font-family:'Nunito';font-style:normal;font-weight:400 800;src:url(data:font/woff2;base64,__NUNITO__) format('woff2')}
:root{
  --teal:#0E7C7B; --teal-d:#0A5C5B; --teal-l:#D8ECEB;
  --sunny:#FFD23F; --sunny-l:#FFF3C7; --sunny-d:#E0A800;
  --coral:#FF6B6B; --coral-l:#FFE1E1;
  --sky:#4EA5D9; --sky-l:#DCEBF7;
  --ink:#1B2A41; --ink-2:#3F5169; --ink-3:#6B7A8D;
  --paper:#FFFDF7; --line:#D9D6CB;
  --head:'Baloo 2','Nunito',system-ui,sans-serif;
  --body:'Nunito',system-ui,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;overflow:hidden;background:#8A8A8A}
body{font-family:var(--body);color:var(--ink);font-weight:500;-webkit-font-smoothing:antialiased}
#deck{position:absolute;inset:0;display:grid;place-items:center}
.slide{display:none;width:1280px;height:720px;background:var(--paper);position:relative;overflow:hidden}
.slide.active{display:block}
.stage{position:absolute;inset:0;padding:54px 72px 44px;display:flex;flex-direction:column}
.kicker{font-family:var(--head);font-size:13px;letter-spacing:.16em;text-transform:uppercase;font-weight:800;color:var(--teal)}
h1{font-family:var(--head);font-weight:800;font-size:86px;line-height:.95;letter-spacing:-.01em}
h2{font-family:var(--head);font-weight:800;font-size:47px;line-height:1.06;margin-top:8px;max-width:1060px}
.rule{width:84px;height:7px;background:var(--sunny);border-radius:4px;margin-top:14px}
.body{flex:1;display:flex;align-items:center;justify-content:center;gap:26px;margin-top:14px}
.card{background:#fff;border:3px solid var(--ink);border-radius:20px;padding:18px 22px}
.card .t{font-family:var(--head);font-weight:800;font-size:25px;line-height:1.15}
.card .d{font-size:18px;line-height:1.5;color:var(--ink-2);margin-top:7px}
.card.sunny{background:var(--sunny-l);border-color:var(--sunny-d)}
.card.coral{background:var(--coral-l);border-color:var(--coral)}
.card.sky{background:var(--sky-l);border-color:var(--sky)}
.card.teal{background:var(--teal-l);border-color:var(--teal)}
.badge{width:38px;height:38px;border-radius:50%;border:3px solid var(--ink);display:grid;place-items:center;
       font-family:var(--head);font-weight:800;font-size:19px;flex:none}
.pill{display:inline-flex;align-items:center;gap:7px;border:2.5px solid var(--ink);border-radius:999px;padding:5px 15px;
      font-family:var(--head);font-weight:800;font-size:15px;background:#fff}
.pill.teal{background:var(--teal);color:#fff;border-color:var(--teal)}
.pill.sunny{background:var(--sunny)}
.pill.sky{background:var(--sky);color:#fff;border-color:var(--sky)}
.pill.coral{background:var(--coral)}
.pills{display:flex;gap:10px;flex-wrap:wrap}
.num{font-family:var(--head);font-weight:800;line-height:.9}
.cap{font-size:19px;color:var(--ink-2);margin-top:12px;font-weight:700}
.milo{display:flex;gap:14px;align-items:center}
.bubble{position:relative;background:var(--sunny);border:3px solid var(--ink);border-radius:18px;padding:12px 18px;
        font-family:var(--head);font-weight:700;font-size:20px;line-height:1.35}
.bubble:before{content:"";position:absolute;left:-11px;top:16px;width:16px;height:16px;background:var(--sunny);
        border-left:3px solid var(--ink);border-bottom:3px solid var(--ink);transform:rotate(45deg)}
.foot{display:flex;justify-content:space-between;align-items:center;font-family:var(--head);font-size:12px;
      letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);font-weight:800;margin-top:10px}
#hud{position:absolute;right:16px;bottom:12px;font-family:var(--head);font-size:13px;font-weight:800;color:#fff;
     background:var(--ink);border-radius:999px;padding:4px 12px;opacity:.75}
#notes{position:absolute;left:0;right:0;bottom:0;max-height:38%;overflow:auto;background:#111;color:#eee;
       font:14px/1.5 ui-monospace,Menlo,Consolas,monospace;padding:14px 18px;display:none;z-index:9}
#notes.on{display:block}
@media screen and (max-width:900px){
  #deck{display:block;overflow:auto}
  .slide{width:100vw;height:auto;min-height:100vh}
  .stage{position:relative;inset:auto}
}
@media print{
  @page{size:1280px 720px;margin:0}
  html,body{background:#fff;overflow:visible}
  #deck{position:static;display:block}
  #hud,#notes{display:none!important}
  .slide{display:block!important;width:1280px;height:720px;page-break-after:always;break-after:page}
  .slide:last-of-type{page-break-after:auto;break-after:auto}
}
"""

MILO = """<svg viewBox="0 0 120 130" role="img" aria-label="Milo the MioPod">
  <path d="M60 0 l3.4 8.2 8.6 1.2 -6.3 6.1 1.6 8.6 -7.3-4.4 -7.3 4.4 1.6-8.6 -6.3-6.1 8.6-1.2z" fill="#FFD23F" stroke="#1B2A41" stroke-width="2.4" stroke-linejoin="round"/>
  <path d="M60 26 v-6" stroke="#1B2A41" stroke-width="3" stroke-linecap="round"/>
  <rect x="20" y="26" width="80" height="86" rx="22" fill="#0E7C7B" stroke="#1B2A41" stroke-width="3"/>
  <rect x="33" y="45" width="54" height="34" rx="12" fill="#FFFDF7" stroke="#1B2A41" stroke-width="3"/>
  <circle cx="48" cy="62" r="5" fill="#1B2A41"/><circle cx="72" cy="62" r="5" fill="#1B2A41"/>
  <path d="M50 71 q10 8 20 0" stroke="#1B2A41" stroke-width="3" fill="none" stroke-linecap="round"/>
  <rect x="40" y="88" width="40" height="8" rx="4" fill="#FFD23F" stroke="#1B2A41" stroke-width="2.4"/>
  <rect x="46" y="112" width="10" height="14" rx="4" fill="#1B2A41"/>
  <rect x="64" y="112" width="10" height="14" rx="4" fill="#1B2A41"/>
</svg>"""

milo_big = MILO.replace('<svg ', '<svg width="200" height="217" ')
milo_small = MILO.replace('<svg ', '<svg width="74" height="80" ')

STEPS = [
    ("Data collection", "You move; the app records 2 seconds of signal.", "var(--teal)", "#fff"),
    ("Labelling", "That recording gets the name of the movement.", "var(--sky)", "#fff"),
    ("Representation", "The recording becomes a few numbers: min, mean, max.", "var(--sunny)", "var(--ink)"),
    ("Training", "The model is built from your labelled examples.", "var(--coral)", "var(--ink)"),
    ("Testing / prediction", "A new movement is named — or comes back unknown.", "var(--teal-d)", "#fff"),
]

pipeline = ""
for i, (name, desc, color, txtc) in enumerate(STEPS):
    arrow = '<div style="font-family:var(--head);font-size:30px;color:var(--ink-3);align-self:center">›</div>' if i < 4 else ""
    pipeline += f"""      <div class="card" style="flex:1;border-color:{color};display:flex;flex-direction:column;gap:10px;min-height:300px;justify-content:center">
        <span class="badge" style="background:{color};color:{txtc}">{i+1}</span>
        <div class="t" style="font-size:21px">{name}</div>
        <div style="font-size:16px;line-height:1.45;color:var(--ink-2)">{desc}</div></div>{arrow}\n"""

NUMBERLINE = """
<svg viewBox="0 0 1000 280" width="1000" height="280" role="img" aria-label="Number line 0 to 10 showing min 4, mean 7, value 8 and max 9">
  <line x1="60" y1="130" x2="940" y2="130" stroke="#1B2A41" stroke-width="4" stroke-linecap="round"/>
  <line x1="60" y1="120" x2="60" y2="140" stroke="#1B2A41" stroke-width="4"/>
  <line x1="940" y1="120" x2="940" y2="140" stroke="#1B2A41" stroke-width="4"/>
  <line x1="500" y1="122" x2="500" y2="138" stroke="#1B2A41" stroke-width="3"/>
  <text x="52" y="170" font-family="Nunito" font-size="18" font-weight="800" fill="#6B7A8D">0</text>
  <text x="492" y="170" font-family="Nunito" font-size="18" font-weight="800" fill="#6B7A8D">5</text>
  <text x="922" y="170" font-family="Nunito" font-size="18" font-weight="800" fill="#6B7A8D">10</text>
  <circle cx="412" cy="130" r="13" fill="#FF6B6B" stroke="#1B2A41" stroke-width="3"/>
  <text x="412" y="96" text-anchor="middle" font-family="Nunito" font-size="20" font-weight="800" fill="#1B2A41">min 4</text>
  <circle cx="676" cy="130" r="16" fill="#0E7C7B" stroke="#1B2A41" stroke-width="3"/>
  <text x="676" y="96" text-anchor="middle" font-family="Baloo 2" font-size="22" font-weight="800" fill="#0A5C5B">mean 7</text>
  <circle cx="764" cy="130" r="12" fill="#4EA5D9" stroke="#1B2A41" stroke-width="3"/>
  <text x="764" y="170" text-anchor="middle" font-family="Nunito" font-size="19" font-weight="800" fill="#1B2A41">8</text>
  <circle cx="852" cy="130" r="13" fill="#FFD23F" stroke="#1B2A41" stroke-width="3"/>
  <text x="852" y="96" text-anchor="middle" font-family="Nunito" font-size="20" font-weight="800" fill="#1B2A41">max 9</text>
  <path d="M412 200 L676 200" stroke="#FF6B6B" stroke-width="3" stroke-dasharray="7 6"/>
  <path d="M676 200 L852 200" stroke="#E0A800" stroke-width="3" stroke-dasharray="7 6"/>
  <text x="412" y="232" text-anchor="middle" font-family="Nunito" font-size="16" font-weight="800" fill="#C0392B">3 below the mean</text>
  <text x="852" y="232" text-anchor="middle" font-family="Nunito" font-size="16" font-weight="800" fill="#8A6A00">2 above the mean</text>
</svg>"""

TWO_MEANS = """
<svg viewBox="0 0 1000 280" width="1000" height="280" role="img" aria-label="Number line 0 to 10 with Wrist down mean at 2, a new recording at 6, and Wrist up mean at 7">
  <line x1="60" y1="130" x2="940" y2="130" stroke="#1B2A41" stroke-width="4" stroke-linecap="round"/>
  <line x1="60" y1="120" x2="60" y2="140" stroke="#1B2A41" stroke-width="4"/>
  <line x1="940" y1="120" x2="940" y2="140" stroke="#1B2A41" stroke-width="4"/>
  <text x="52" y="170" font-family="Nunito" font-size="18" font-weight="800" fill="#6B7A8D">0</text>
  <text x="922" y="170" font-family="Nunito" font-size="18" font-weight="800" fill="#6B7A8D">10</text>
  <circle cx="236" cy="130" r="16" fill="#FF6B6B" stroke="#1B2A41" stroke-width="3"/>
  <text x="236" y="96" text-anchor="middle" font-family="Baloo 2" font-size="21" font-weight="800" fill="#C0392B">Wrist down · 2</text>
  <circle cx="588" cy="130" r="13" fill="#FFD23F" stroke="#1B2A41" stroke-width="3"/>
  <text x="588" y="170" text-anchor="middle" font-family="Nunito" font-size="19" font-weight="800" fill="#1B2A41">new · 6</text>
  <circle cx="676" cy="130" r="16" fill="#0E7C7B" stroke="#1B2A41" stroke-width="3"/>
  <text x="676" y="96" text-anchor="middle" font-family="Baloo 2" font-size="21" font-weight="800" fill="#0A5C5B">Wrist up · 7</text>
  <path d="M236 200 L588 200" stroke="#FF6B6B" stroke-width="3" stroke-dasharray="8 6"/>
  <path d="M588 200 L676 200" stroke="#0E7C7B" stroke-width="4" stroke-dasharray="8 6"/>
  <text x="236" y="232" text-anchor="middle" font-family="Nunito" font-size="16" font-weight="800" fill="#C0392B">4 away</text>
  <text x="676" y="232" text-anchor="middle" font-family="Nunito" font-size="16" font-weight="800" fill="#0A5C5B">1 away</text>
</svg>"""

LABEL_FIG = """
<svg viewBox="0 0 470 230" width="470" height="230" role="img" aria-label="A two second recording with a label tag reading Wrist up">
  <rect x="10" y="40" width="300" height="120" rx="14" fill="#fff" stroke="#1B2A41" stroke-width="3"/>
  <path d="M32 118 l16 -24 15 32 19 -38 17 28 15 -16 17 24 19 -32 15 28 17 -20 15 30 19 -26 15 20"
        fill="none" stroke="#4EA5D9" stroke-width="3.4" stroke-linejoin="round"/>
  <text x="16" y="28" font-family="Nunito" font-size="16" font-weight="800" fill="#6B7A8D">2 seconds of signal</text>
  <path d="M310 100 L352 100" stroke="#1B2A41" stroke-width="3"/>
  <rect x="352" y="78" width="106" height="44" rx="12" fill="#FFD23F" stroke="#1B2A41" stroke-width="3"/>
  <text x="405" y="107" text-anchor="middle" font-family="Baloo 2" font-size="19" font-weight="800" fill="#1B2A41">Wrist up</text>
  <text x="405" y="150" text-anchor="middle" font-family="Nunito" font-size="15" font-weight="800" fill="#6B7A8D">the label</text>
</svg>"""

SQUIGGLE = """
<svg viewBox="0 0 400 96" width="400" height="96" role="img" aria-label="A noisy signal trace">
  <path d="M6 60 l14 -26 12 34 14 -38 12 30 12 -16 14 26 14 -34 12 28 12 -20 14 30 14 -26 12 18 14 -30 12 24 14 -18 12 26 14 -32 12 20 14 -12 12 24 14 -20"
        fill="none" stroke="#4EA5D9" stroke-width="3" stroke-linejoin="round"/>
</svg>"""

slides = []

slides.append(f"""
<section class="slide active">
  <div class="stage">
    <div class="kicker">EMG lab · grades 9–10</div>
    <div class="body" style="align-items:center;gap:40px">
      <div style="flex:1">
        <h1>From Muscle<br>to Machine</h1>
        <div class="rule"></div>
        <div style="margin-top:20px;font-size:23px;color:var(--ink-2);max-width:640px;line-height:1.4">
          How a muscle signal becomes numbers, and how those numbers let a computer guess what you did.</div>
        <div class="pills" style="margin-top:26px">
          <span class="pill teal">3 ideas</span>
          <span class="pill sunny">5 pipeline steps</span>
          <span class="pill sky">1 worked example</span>
        </div>
      </div>
      <div>{milo_big}</div>
    </div>
    <div class="foot"><span>From Muscle to Machine</span><span>1 / 9</span></div>
  </div>
</section>""")

slides.append(f"""
<section class="slide">
  <div class="stage">
    <div class="kicker">1 · the signal</div>
    <h2>Your muscle is already electric</h2>
    <div class="rule"></div>
    <div class="body" style="flex-direction:column;gap:18px">
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px;width:100%">
        <div class="card sky" style="min-height:236px;display:flex;flex-direction:column;justify-content:center">
          <div class="badge" style="background:var(--sky);color:#fff">1</div>
          <div class="t" style="margin-top:10px">A nerve fires</div>
          <div class="d">Your brain sends a signal along a nerve to the muscle.</div></div>
        <div class="card sunny" style="min-height:236px;display:flex;flex-direction:column;justify-content:center">
          <div class="badge" style="background:var(--sunny)">2</div>
          <div class="t" style="margin-top:10px">Fibres make voltage</div>
          <div class="d">Every muscle fibre the nerve controls makes a tiny electrical change.</div></div>
        <div class="card coral" style="min-height:236px;display:flex;flex-direction:column;justify-content:center">
          <div class="badge" style="background:var(--coral)">3</div>
          <div class="t" style="margin-top:10px">The sensor adds them up</div>
          <div class="d">Electrodes on your skin record the combined activity of thousands of fibres.</div></div>
      </div>
      <div class="milo">{milo_small}
        <div class="bubble">That combined signal is called <b>surface EMG</b> — electromyography.</div></div>
    </div>
    <div class="foot"><span>The signal</span><span>2 / 9</span></div>
  </div>
</section>""")

slides.append(f"""
<section class="slide">
  <div class="stage">
    <div class="kicker">1 · the signal</div>
    <h2>EMG records activity — not effort</h2>
    <div class="rule"></div>
    <div class="body" style="gap:22px">
      <div class="card teal" style="flex:1;min-height:300px;display:flex;flex-direction:column;justify-content:center">
        <div class="t" style="font-size:26px">It does record</div>
        <div class="d" style="font-size:19px;line-height:1.65;margin-top:10px">
          ● electrical activity of many muscle fibres<br>
          ● a noisy line that changes over time<br>
          ● differences between movements</div>
      </div>
      <div class="card coral" style="flex:1;min-height:300px;display:flex;flex-direction:column;justify-content:center">
        <div class="t" style="font-size:26px">It does not record</div>
        <div class="d" style="font-size:19px;line-height:1.65;margin-top:10px">
          ● how strong you are<br>
          ● your thoughts, or your brain directly<br>
          ● one named muscle — the sensor sees a mix</div>
      </div>
    </div>
    <div class="cap">A bigger squiggle usually means a busier muscle — not a stronger one.</div>
    <div class="foot"><span>The signal</span><span>3 / 9</span></div>
  </div>
</section>""")

slides.append(f"""
<section class="slide">
  <div class="stage">
    <div class="kicker">2 · the pipeline</div>
    <h2>Five steps turn a movement into a guess</h2>
    <div class="rule"></div>
    <div class="body">
      <div style="display:flex;gap:8px;width:100%">{pipeline}</div>
    </div>
    <div class="cap">Each step depends on the one before it — a mistake at step 2 shows up at step 5.</div>
    <div class="foot"><span>Pipeline</span><span>4 / 9</span></div>
  </div>
</section>""")

slides.append(f"""
<section class="slide">
  <div class="stage">
    <div class="kicker">2 · the pipeline</div>
    <h2>A label is a claim about a recording</h2>
    <div class="rule"></div>
    <div class="body" style="gap:34px;align-items:center">
      {LABEL_FIG}
      <div style="flex:1;display:flex;flex-direction:column;gap:16px">
        <div class="card" style="border-color:var(--teal)">
          <div class="t">The name comes from the instruction</div>
          <div class="d">You were asked for “Wrist up”, so that recording is saved <b>with that name</b>.
            The app does not work the name out — it stores the one you were given.</div>
        </div>
        <div class="card sunny">
          <div class="t">Before labels, the app knows nothing</div>
          <div class="d">It has never seen a Wrist up or a Wrist down. Everything it knows came from your labelled examples.</div>
        </div>
      </div>
    </div>
    <div class="foot"><span>Labels · step 2</span><span>5 / 9</span></div>
  </div>
</section>""")

slides.append(f"""
<section class="slide">
  <div class="stage">
    <div class="kicker">2 · the pipeline</div>
    <h2>One recording becomes a few numbers</h2>
    <div class="rule"></div>
    <div class="body" style="gap:26px">
      <div class="card" style="flex:1.1;min-height:340px;display:flex;flex-direction:column;justify-content:center">
        <div class="t">What the app saves</div>
        <div class="d">Two seconds of signal — hundreds of values, too many to compare by eye.</div>
        <div style="margin-top:10px">{SQUIGGLE}</div>
      </div>
      <div style="font-family:var(--head);font-size:44px;color:var(--ink-3)">→</div>
      <div style="flex:1;display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;min-height:340px">
        <div class="card coral" style="text-align:center;display:flex;flex-direction:column;justify-content:center">
          <div class="d" style="margin:0;font-weight:800">min</div>
          <div class="num" style="font-size:52px;margin-top:6px">4</div></div>
        <div class="card teal" style="text-align:center;display:flex;flex-direction:column;justify-content:center">
          <div class="d" style="margin:0;font-weight:800">mean</div>
          <div class="num" style="font-size:52px;margin-top:6px">7</div></div>
        <div class="card sunny" style="text-align:center;display:flex;flex-direction:column;justify-content:center">
          <div class="d" style="margin:0;font-weight:800">max</div>
          <div class="num" style="font-size:52px;margin-top:6px">9</div></div>
      </div>
    </div>
    <div class="cap">Those three numbers are the <b>representation</b> — something a model can compare.</div>
    <div class="foot"><span>Representation · step 3</span><span>6 / 9</span></div>
  </div>
</section>""")

slides.append(f"""
<section class="slide">
  <div class="stage">
    <div class="kicker">3 · worked example</div>
    <h2>One example: 4, 9, 8</h2>
    <div class="rule"></div>
    <div class="body" style="flex-direction:column;gap:6px">
      <div style="display:flex;gap:14px;align-items:center;font-size:20px;font-weight:800;margin-bottom:2px">
        <span class="pill coral">min = 4</span>
        <span class="pill" style="background:var(--teal-l);border-color:var(--teal)">mean = (4 + 9 + 8) ÷ 3 = 21 ÷ 3 = 7</span>
        <span class="pill sunny">max = 9</span>
      </div>
      {NUMBERLINE}
    </div>
    <div class="cap">Two of these numbers tell you the edges; the mean tells you the middle.</div>
    <div class="foot"><span>min 4 · mean 7 · max 9</span><span>7 / 9</span></div>
  </div>
</section>""")

slides.append(f"""
<section class="slide">
  <div class="stage">
    <div class="kicker">3 · worked example</div>
    <h2>Two means are enough to make a model</h2>
    <div class="rule"></div>
    <div class="body" style="flex-direction:column;gap:10px">
      {TWO_MEANS}
      <div style="display:flex;gap:16px;width:100%">
        <div class="card teal" style="flex:1"><div class="t" style="font-size:20px">The rule</div>
          <div class="d">Compare the new recording’s mean with each stored mean, and pick the closer one.</div></div>
        <div class="card" style="flex:1;border-color:var(--sky)"><div class="t" style="font-size:20px">Here</div>
          <div class="d">6 is 1 away from 7 and 4 away from 2 → predict <b>Wrist up</b>.</div></div>
      </div>
    </div>
    <div class="foot"><span>Training sets the means · testing compares a new recording</span><span>8 / 9</span></div>
  </div>
</section>""")

slides.append(f"""
<section class="slide">
  <div class="stage">
    <div class="kicker">3 · worked example</div>
    <h2>In between, the honest answer is “unknown”</h2>
    <div class="rule"></div>
    <div class="body" style="gap:36px">
      <div style="flex:1;display:flex;flex-direction:column;gap:16px">
        <div class="card coral"><div class="t">A mean of exactly 4.5</div>
          <div class="d">Equally far from 2 and from 7. A one-number rule has nothing to prefer — so it says
            <b>unknown</b>, instead of flipping a coin.</div></div>
        <div class="card" style="border-color:var(--teal)"><div class="t">And the model is only as good as step 2</div>
          <div class="d">A wrong label, or a recording that did not match the movement, gives a wrong mean —
            and a wrong guess.</div></div>
      </div>
      <div>{milo_big}</div>
    </div>
    <div class="cap">Next: your turn — put the five steps back in order.</div>
    <div class="foot"><span>Wrap-up</span><span>9 / 9</span></div>
  </div>
</section>""")

NOTES = [
 "Frame the session: the computer learns from YOUR arm. Nothing here is magic — five steps plus arithmetic.",
 "Ask: what would have to be true for a computer to 'know' you bent your wrist? Draw out that muscle makes electricity, not force.",
 "Key correction: signal size is not strength. Expect 'the sensor measures how hard I squeezed' — correct it here.",
 "Ask students to predict the order before revealing 1–5. Data collection must be first; testing/prediction last.",
 "Ask: where did the name 'Wrist up' come from? The instruction, not the app. That is the supervised-learning idea.",
 "Ask: why three numbers instead of the whole squiggle? Because comparing needs something short and stable.",
 "Work the mean aloud: 4+9 = 13, +8 = 21, 21 ÷ 3 = 7. Then ask which value is closest to the mean (8) and furthest (4).",
 "This is the payoff: the two means ARE the model — no hidden brain. Ask what happens if the new recording is a sloppy movement.",
 "Close on honesty: 'unknown' is designed, not a bug. Then hand out the ordering worksheet.",
]

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>From Muscle to Machine — EMG basics and the ML pipeline</title>
<style>{CSS.replace('__BALOO__', b64['baloo2.woff2']).replace('__NUNITO__', b64['nunito.woff2'])}</style>
</head>
<body>
<div id="deck">
{''.join(slides)}
</div>
<div id="hud">1 / 9</div>
<div id="notes"></div>
<script>
var NOTES = {NOTES!r};
var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
var i = 0, notesOn = false;
function show(n){{
  i = Math.max(0, Math.min(slides.length - 1, n));
  slides.forEach(function(s, k){{ s.classList.toggle('active', k === i); }});
  document.getElementById('hud').textContent = (i + 1) + ' / ' + slides.length;
  if (notesOn) {{ document.getElementById('notes').textContent = NOTES[i] || ''; }}
}}
document.addEventListener('keydown', function(e){{
  if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {{ e.preventDefault(); show(i + 1); }}
  if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{ e.preventDefault(); show(i - 1); }}
  if (e.key === 'n' || e.key === 'N') {{
    notesOn = !notesOn;
    document.getElementById('notes').classList.toggle('on', notesOn);
    document.getElementById('notes').textContent = NOTES[i] || '';
  }}
}});
show(0);
</script>
</body>
</html>
"""

out = pathlib.Path("/root/emg_deck/index.html")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(html)
print("wrote", out, len(html), "bytes")