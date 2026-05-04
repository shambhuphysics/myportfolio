(function () {
  var titles = [
    "High-Throughput DFT Screening & ML",
    "AI for Earth Observation",
    "Ab Initio Molecular Dynamics — Earth's Core",
    "Quantum Transport Simulations",
    "Electronic Structure & Phonon Properties",
    "Agentic AI Framework Design",
    "End-to-End ML Engineering Pipeline"
  ];

  var n = SLIDE_COUNT, cur = 1, active = "a", delay = 2000, timer;

  function show(i) {
    cur = ((i - 1 + n) % n) + 1;
    var ns = active === "a" ? "b" : "a";
    document.getElementById("slide-" + ns).src = "../slides/pngs/slide-" + cur + ".png";
    document.getElementById("slide-" + ns).style.opacity = "1";
    document.getElementById("slide-" + active).style.opacity = "0";
    active = ns;
    var el = document.getElementById("slide-title");
    el.textContent = titles[cur - 1];
    el.style.animation = "none";
    void el.offsetHeight;
    el.style.animation = "title-in 0.5s ease forwards";
    document.getElementById("slide-counter").textContent = cur + " / " + n;
  }

  function next() { show(cur + 1); }
  function prev() { show(cur - 1); }
  function restart() { clearInterval(timer); timer = setInterval(next, delay); }

  timer = setInterval(next, delay);

  document.getElementById("slide-next").addEventListener("click", function () { next(); restart(); });
  document.getElementById("slide-prev").addEventListener("click", function () { prev(); restart(); });
  document.getElementById("slides-wrap").addEventListener("click", function (e) {
    if (e.target.id !== "slide-prev" && e.target.id !== "slide-next") { next(); restart(); }
  });
})();
