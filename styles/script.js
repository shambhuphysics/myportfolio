$(document).ready(function () {
  $(window).scroll(function () {
    if (this.scrollY > 20) {
      $(".navbar").addClass("sticky");
    } else {
      $(".navbar").removeClass("sticky");
    }

    if (this.scrollY > 500) {
      $(".scroll-up-btn").addClass("show");
    } else {
      $(".scroll-up-btn").removeClass("show");
    }
  });

  $(".scroll-up-btn").click(function () {
    $("html").animate({ scrollTop: 0 });
    $("html").css("scrollBehavior", "auto");
  });

  $(".navbar .menu li a").click(function () {
    $("html").css("scrollBehavior", "smooth");
  });

  $(".menu-btn").click(function () {
    $(".navbar .menu").toggleClass("active");
    $(".menu-btn i").toggleClass("active");
  });

  // mobile: tap dropdown parent to accordion-open
  $('.navbar .menu li.has-dropdown > a').on('click', function(e) {
    if ($(window).width() <= 947) {
      e.preventDefault();
      $(this).parent().toggleClass('open')
             .siblings('.has-dropdown').removeClass('open');
    }
  });

  // mobile: tap submenu parent to accordion-open
  $('.navbar .menu li.has-submenu > a').on('click', function(e) {
    if ($(window).width() <= 947) {
      e.preventDefault();
      $(this).parent().toggleClass('open')
             .siblings('.has-submenu').removeClass('open');
    }
  });

  // close dropdowns when clicking outside the navbar
  $(document).on('click', function(e) {
    if (!$(e.target).closest('.navbar').length) {
      $('.has-dropdown, .has-submenu').removeClass('open');
    }
  });

  // close mobile menu when a non-dropdown link is tapped
  $('.navbar .menu li:not(.has-dropdown) > a').on('click', function() {
    if ($(window).width() <= 947) {
      $('.navbar .menu').removeClass('active');
      $('.menu-btn i').removeClass('active');
    }
  });

  var typed = new Typed(".typing", {
    strings: [
      "PhD Researcher",
      "Data Scientist",
      "Computational Physicist",
      "Condensed Matter Physicist",
    ],
    typeSpeed: 10,
    backSpeed: 60,
    loop: true,
  });

});

// ── Scroll progress bar ──────────────────────────────────────────
(function () {
  var bar = document.getElementById('scroll-progress');
  if (!bar) return;
  window.addEventListener('scroll', function () {
    var total = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.width = (window.scrollY / total * 100).toFixed(2) + '%';
  }, { passive: true });
})();

// ── Site search ──────────────────────────────────────────────────
(function () {
  var trigger   = document.getElementById('searchTrigger');
  var overlay   = document.getElementById('searchOverlay');
  var input     = document.getElementById('searchInput');
  var closeBtn  = document.getElementById('searchClose');
  var resultsEl = document.getElementById('searchResults');
  if (!trigger || !overlay) return;

  // Static index: sections + sub-pages
  var index = [
    { title: 'About Me',             sub: 'Section',                      type: 'Section',     icon: 'fas fa-user',            href: '#about'              },
    { title: 'Experience',           sub: 'About section',                type: 'Section',     icon: 'fas fa-briefcase',       href: '#experience'         },
    { title: 'Education',            sub: 'About section',                type: 'Section',     icon: 'fas fa-graduation-cap',  href: '#education'          },
    { title: 'Skills',               sub: 'Section',                      type: 'Section',     icon: 'fas fa-code',            href: '#skills'             },
    { title: 'Publications',         sub: 'Section',                      type: 'Section',     icon: 'fas fa-book-open',       href: '#publications'       },
    { title: 'Contact',              sub: 'Section',                      type: 'Section',     icon: 'fas fa-envelope',        href: '#contact'            },
    { title: 'Awards & Recognition', sub: 'Certifications · Peer review', type: 'Page',        icon: 'fas fa-trophy',          href: 'awards.html'         },
    { title: 'Gallery',              sub: 'Photo timeline 2018–2024',     type: 'Page',        icon: 'fas fa-images',          href: 'gallery.html'        },
    { title: 'Machine Learning',     sub: 'Library',                      type: 'Page',        icon: 'fas fa-robot',           href: 'machine_learning.html' },
    { title: 'Physics & Chemistry',  sub: 'Library',                      type: 'Page',        icon: 'fas fa-atom',            href: 'physics.html'        },
    { title: 'Quantum Computing',    sub: 'Library',                      type: 'Page',        icon: 'fas fa-qrcode',          href: 'quantum.html'        },
    { title: 'Useful Sites',         sub: 'Resources',                    type: 'Page',        icon: 'fas fa-globe',           href: 'useful_sites.html'   },
    { title: 'Wellbeing',            sub: 'Resources',                    type: 'Page',        icon: 'fas fa-heart',           href: 'wellbeing.html'      },
    { title: 'STEM Research Projects', sub: 'Research',                   type: 'Page',        icon: 'fas fa-flask',           href: 'projects.html'       },
    { title: 'MLOps Projects',       sub: 'Research',                     type: 'Page',        icon: 'fas fa-cogs',            href: 'mlops.html'          },
  ];

  // Publications — built from DOM
  document.querySelectorAll('.pub-card').forEach(function (card) {
    var cite    = card.querySelector('.pub-citation');
    var journal = card.querySelector('.pub-journal');
    var year    = card.querySelector('.pub-year');
    if (!cite) return;
    index.push({
      title: cite.textContent.trim().slice(0, 90),
      sub:   [(journal && journal.textContent.trim()), (year && year.textContent.trim())].filter(Boolean).join(' · '),
      type:  'Publication', icon: 'fas fa-file-alt', href: '#publications',
    });
  });

  // Skills — built from DOM
  document.querySelectorAll('.stack-cat-block').forEach(function (block) {
    var cat = (block.querySelector('.scat-title') || {}).textContent || 'Skills';
    block.querySelectorAll('.stk-badge').forEach(function (badge) {
      index.push({ title: badge.textContent.trim(), sub: cat.trim(), type: 'Skill', icon: 'fas fa-tools', href: '#skills' });
    });
  });

  // Experience & Education — built from DOM
  document.querySelectorAll('.tl-item').forEach(function (item) {
    var role    = (item.querySelector('.tl-role') || {}).textContent || '';
    var org     = (item.querySelector('.tl-org')  || {}).textContent || '';
    var section = item.closest('#experience') ? 'Experience' : 'Education';
    if (!role) return;
    index.push({
      title: role.trim(), sub: org.trim(), type: section,
      icon:  section === 'Experience' ? 'fas fa-briefcase' : 'fas fa-graduation-cap',
      href:  '#' + section.toLowerCase(),
    });
  });

  // ── Deep index: fetch all sub-pages in background ──
  var PAGE_DEFS = [
    { file: 'machine_learning.html', label: 'Machine Learning',    icon: 'fas fa-robot'  },
    { file: 'physics.html',          label: 'Physics & Chemistry', icon: 'fas fa-atom'   },
    { file: 'quantum.html',          label: 'Quantum Computing',   icon: 'fas fa-qrcode' },
    { file: 'useful_sites.html',     label: 'Useful Sites',        icon: 'fas fa-globe'  },
    { file: 'projects.html',         label: 'STEM Projects',       icon: 'fas fa-flask'  },
    { file: 'mlops.html',            label: 'MLOps Projects',      icon: 'fas fa-cogs'   },
    { file: 'awards.html',           label: 'Awards',              icon: 'fas fa-trophy' },
    { file: 'wellbeing.html',        label: 'Wellbeing',           icon: 'fas fa-heart'  },
  ];

  function addUnique(entry) {
    var key = entry.title + '|' + entry.href;
    if (!addUnique._seen) addUnique._seen = {};
    if (addUnique._seen[key]) return;
    addUnique._seen[key] = true;
    index.push(entry);
  }

  function extractPage(html, def) {
    var doc = new DOMParser().parseFromString(html, 'text/html');
    var selectors = [
      // Category / section headings
      { sel: '.category h2, .category h3', field: 'title' },
      // Course names (links and plain spans)
      { sel: '.course-name a, .course-name > span', field: 'title' },
      // Specialization block titles
      { sel: '.spec-title', field: 'title' },
      // Link grid items
      { sel: '.link-item a', field: 'title' },
      // Project cards
      { sel: '.project-title', field: 'title' },
      // Project descriptions
      { sel: '.project-body p', field: 'title' },
      // Tag lists
      { sel: '.tag-list .tag', field: 'sub' },
    ];
    selectors.forEach(function (s) {
      doc.querySelectorAll(s.sel).forEach(function (el) {
        var text = el.textContent.replace(/\s+/g, ' ').trim();
        if (text.length < 4) return;
        var entry = { title: text.slice(0, 120), sub: def.label, type: def.label, icon: def.icon, href: def.file };
        if (s.field === 'sub') { entry.title = def.label; entry.sub = text.slice(0, 80); }
        addUnique(entry);
      });
    });
  }

  PAGE_DEFS.forEach(function (def) {
    fetch(def.file)
      .then(function (r) { return r.ok ? r.text() : Promise.reject(); })
      .then(function (html) { extractPage(html, def); })
      .catch(function () {});
  });

  // ── Scoring ──
  function score(r, lq, words) {
    var hay = (r.title + ' ' + r.sub).toLowerCase();
    if (hay.includes(lq)) return 10;                        // exact phrase
    var matched = words.filter(function (w) { return hay.includes(w); }).length;
    return matched > 0 ? matched / words.length * 5 : 0;   // partial word match
  }

  // ── Open / close ──
  function openSearch() {
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
    setTimeout(function () { input.focus(); }, 40);
    render('');
  }
  function closeSearch() {
    overlay.classList.remove('active');
    document.body.style.overflow = '';
    input.value = '';
    resultsEl.innerHTML = '';
  }

  trigger.addEventListener('click', openSearch);
  closeBtn.addEventListener('click', closeSearch);
  overlay.addEventListener('click', function (e) { if (e.target === overlay) closeSearch(); });

  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement.tagName !== 'INPUT') { e.preventDefault(); openSearch(); }
    if (!overlay.classList.contains('active')) return;
    if (e.key === 'Escape') { closeSearch(); return; }
    var items   = Array.from(resultsEl.querySelectorAll('.search-result'));
    var focused = resultsEl.querySelector('.search-result.focused');
    var idx     = items.indexOf(focused);
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (idx < items.length - 1) { if (focused) focused.classList.remove('focused'); items[idx + 1].classList.add('focused'); items[idx + 1].scrollIntoView({ block: 'nearest' }); }
    }
    if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (idx > 0) { if (focused) focused.classList.remove('focused'); items[idx - 1].classList.add('focused'); items[idx - 1].scrollIntoView({ block: 'nearest' }); }
    }
    if (e.key === 'Enter' && focused) { focused.click(); }
  });

  input.addEventListener('input', function () { render(input.value.trim()); });

  function navigate(href) {
    closeSearch();
    if (href.startsWith('#')) {
      var target = document.querySelector(href);
      if (target) setTimeout(function () { target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 160);
    } else {
      window.location.href = href;
    }
  }

  function highlight(text, lq) {
    if (!lq) return text;
    var re = new RegExp('(' + lq.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
    return text.replace(re, '<mark style="background:rgba(220,20,60,0.35);color:#fff;border-radius:2px;">$1</mark>');
  }

  function render(q) {
    var lq    = q.toLowerCase();
    var words = lq.split(/\s+/).filter(Boolean);
    var hits;

    if (!lq) {
      hits = index.filter(function (r) { return r.type === 'Section' || r.type === 'Page'; });
    } else {
      hits = index
        .map(function (r) { return { r: r, s: score(r, lq, words) }; })
        .filter(function (x) { return x.s > 0; })
        .sort(function (a, b) { return b.s - a.s; })
        .slice(0, 15)
        .map(function (x) { return x.r; });
    }

    if (!hits.length) {
      resultsEl.innerHTML = '<div class="search-empty">No results for <strong>"' + q + '"</strong></div>';
      return;
    }
    resultsEl.innerHTML = hits.map(function (r) {
      return '<div class="search-result" data-href="' + r.href + '" tabindex="-1">'
        + '<div class="sr-icon"><i class="' + r.icon + '"></i></div>'
        + '<div class="sr-body"><div class="sr-title">' + highlight(r.title, lq) + '</div>'
        + (r.sub ? '<div class="sr-sub">' + r.sub + '</div>' : '') + '</div>'
        + '<span class="sr-type">' + r.type + '</span>'
        + '</div>';
    }).join('');
    resultsEl.querySelectorAll('.search-result').forEach(function (el) {
      el.addEventListener('click', function () { navigate(el.dataset.href); });
    });
  }
})();

// ── Scroll-reveal with IntersectionObserver ──────────────────────
(function () {
  if (!window.IntersectionObserver) return;

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      var el = entry.target;
      var delay = parseInt(el.dataset.delay || 0);
      setTimeout(function () { el.classList.add('revealed'); }, delay);
      observer.unobserve(el);
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });

  // Groups: selector, slide direction, stagger-ms per sibling within same parent
  var groups = [
    { sel: '.title',              dir: null,    stagger: 0   },
    { sel: '.about-bio',          dir: null,    stagger: 0   },
    { sel: '.tl-heading',         dir: null,    stagger: 0   },
    { sel: '.tl-item',            dir: 'left',  stagger: 85  },
    { sel: '.stack-cat-block',    dir: null,    stagger: 55  },
    { sel: '.pub-card',           dir: 'scale', stagger: 55  },
    { sel: '.blogger-section .card', dir: null, stagger: 0   },
    { sel: '.contact .text',      dir: null,    stagger: 0   },
    { sel: '.contact p',          dir: null,    stagger: 0   },
    { sel: '.contact .row',       dir: 'left',  stagger: 90  },
    { sel: '.blog-main-title',    dir: null,    stagger: 0   },
    { sel: '.blog-section-title', dir: null,    stagger: 0   },
    { sel: '.blog-news',          dir: null,    stagger: 0   },
  ];

  groups.forEach(function (g) {
    var elements = Array.from(document.querySelectorAll(g.sel));
    // Stagger siblings that share the same parent container
    var parentMap = new Map();
    elements.forEach(function (el) {
      var p = el.parentElement;
      if (!parentMap.has(p)) parentMap.set(p, []);
      parentMap.get(p).push(el);
    });
    parentMap.forEach(function (siblings) {
      siblings.forEach(function (el, i) {
        if (el.hasAttribute('data-reveal')) return; // already tagged
        el.setAttribute('data-reveal', '');
        if (g.dir) el.setAttribute('data-dir', g.dir);
        el.dataset.delay = i * g.stagger;
        observer.observe(el);
      });
    });
  });
})();
