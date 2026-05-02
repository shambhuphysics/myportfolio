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

  // close dropdowns when clicking outside the navbar
  $(document).on('click', function(e) {
    if (!$(e.target).closest('.navbar').length) {
      $('.has-dropdown').removeClass('open');
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
