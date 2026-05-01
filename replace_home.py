import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the home section and replace everything from <!-- HOME --> to </section>
# then the about section will follow naturally
home_pattern = re.compile(
    r'  <!-- ========== HOME ========== -->.*?</section>',
    re.DOTALL
)

NEW_HOME = '''  <!-- ========== HOME ========== -->
  <section class="home blog-home" id="home">
    <div class="blog-layout">

      <!-- LEFT SIDEBAR -->
      <aside class="blog-sidebar">
        <div class="sidebar-ucl">
          <img src="https://upload.wikimedia.org/wikipedia/sco/thumb/d/d1/University_College_London_logo.svg/1200px-University_College_London_logo.svg.png" alt="UCL" />
        </div>
        <hr class="sidebar-divider"/>
        <div class="sidebar-profile">
          <img src="images/profile.jpg" alt="Shambhu" class="sidebar-avatar" />
          <div class="sidebar-name">Shambhu Bhandari</div>
          <div class="sidebar-role">PhD Researcher at UCL</div>
          <a class="sidebar-link-visit" href="#about">VISIT PROFILE</a>
        </div>
        <hr class="sidebar-divider"/>
        <nav class="sidebar-nav">
          <a href="projects.html">&#128213; My Presentation slides</a>
          <a href="wellbeing.html">&#127942; Routine: one step towards</a>
          <a href="quantum.html">Q&lt;&psi;| Quantum Algorithm</a>
          <a href="physics.html">&#9883; Physics and Chemistry</a>
          <a href="machine_learning.html">&#127760; Useful Sites</a>
          <a href="gallery.html">&#128444; Gallery</a>
        </nav>
        <hr class="sidebar-divider"/>
        <div class="sidebar-social">
          <a href="https://github.com/shambhuphysics" target="_blank"><i class="fab fa-github"></i></a>
          <a href="https://linkedin.com/in/shambhu-bhandari-sharma-478250176/" target="_blank"><i class="fab fa-linkedin"></i></a>
          <a href="https://sbs2024.blogspot.com/" target="_blank"><i class="fab fa-blogger"></i></a>
        </div>
      </aside>

      <!-- MAIN CONTENT -->
      <main class="blog-main">
        <h1 class="blog-main-title">MY RESEARCH PORTFOLIO</h1>
        <p class="blog-bio">Hi! I am a PhD researcher in Theoretical and Computational Condensed Matter Physics at UCL. My works utilize first-principle calculations and machine learning to explore electronic structural properties, including optomechanical and quantum transport properties of materials. Currently, I focus on the thermoelastic properties of materials under extreme conditions, relevant to planetary cores, developing models to compute high-pressure ab-initio phase diagrams of binary alloys.</p>

        <h2 class="blog-section-title">Ab-initio Phase Diagram Calculations for Al-Mg Alloy</h2>

        <!-- Image Slider -->
        <div class="blog-slider-wrapper">
          <div id="slider">
            <div class="slide"><img src="https://blogger.googleusercontent.com/img/a/AVvXsEhcRacCRY2lkKy80ort_JXjSfgzmuluqbXLwjOirca8NGKY_5iuVzDHMLRb8sp32UyWRs5EeM3Bg6PPOV3y3qK5Z27ATe4RnYV4QNj44aePXNcN_X2QNvcJeXYCHfQXuFikoj6huiTadDzZdft8IcgLM9eAexM3B35lM2qIHwJyuR-Y_ChrQighFCAemYM" alt="Workflow" /></div>
            <div class="slide"><img src="https://blogger.googleusercontent.com/img/a/AVvXsEgQicjmDeozItTrRRD21XwH__A8oJJsU3uLlGhnKp7jj7evrX5tzDjTOlL_kUTqUBloj8VhVFD8qBZCOUO2BVdW2afU1f34nPzYQv8DiCzxgbZ0DLCudAo83HG_kdKlWwiY1ec3utI6wCUqhlf-VTosXlDVlmEgmHoEy0hyEEYNIxrlgoo8N8uZhXAEMEA" alt="Earthcore" /></div>
            <div class="slide"><img src="https://blogger.googleusercontent.com/img/a/AVvXsEho_x6D99fwoUrGAanX3ujjA6DgQzKob-d8w0GjlVfAGEhJoQXBiS9pTaUcgYAMW-U5_hklkeJeeEZB5aZlKzYT8pdimiM1RJ0Ql62Ym8snI5LD49PUuVvzuhdc1mUPtQVwDBnyEVQO-cxY_F0rFT6-R2bTh_5dLbprmjf58W4u-h7L2mfHf_Y9d0MUET4" alt="Instrument" /></div>
            <div class="slide"><img src="https://blogger.googleusercontent.com/img/a/AVvXsEiPBCcVUvOTggJbU0NqH5yIFRcn_Koh9Q8e4fbM4X1KXwSMR17etopLdPm2axYGGnrmOWl2F1efxhNT-B9K6mnvIX3e-O4HLO1GQ5Gp2tzuREQBKWKQSuYvGI4Ye50PpaOZz43axqolfov0hZ8PU6GFPY2t_FqpAhuP4tVBAUAXlcJlhYNxZJ-SLxOLmnU" alt="Phase diagram" /></div>
            <div class="slide"><img src="https://blogger.googleusercontent.com/img/a/AVvXsEhIE4jQAABldj8r71iKXYILJOtRhvVu_NKL5EMAdabkXoKFKdnc_uS7O3K8qUaxhXO4ixUYBrwNigC1cCCP0IhiarR1VeBpac9FttzcRy7kjgEE29mQAQeaUqu6v9SWtSwol6NGQhMQmUqsDAap0aa6Why1S8ymg4A6vUHZRMwmkyHnCMSYja2BAuURZOA" alt="2D material" /></div>
            <div class="slide"><img src="https://blogger.googleusercontent.com/img/a/AVvXsEjLj8XiUgpn4z2OwL8PnP_EC1MdihfL--4j49dxzLC3pBjbvLvpgRAelmDjsDWDFmFUEYFySXhbNQ_B7vWbUT21z-woADMfCJ5RVYlMlixrlHwPL47QvXCrE_6qhQv-iQd1XB_ymckQgEZVg6PU-TDuI-NrJIUWspXkboG4PNn3y7FmwoYUexj8SeVSfhE" alt="Electrides" /></div>
          </div>
        </div>
        <script>
          (function() {
            var sl = document.getElementById("slider");
            var n = 0;
            setInterval(function() {
              if (!sl || !sl.firstElementChild) return;
              n++;
              if (n >= 6) n = 0;
              sl.style.transform = "translateX(-" + (n * sl.firstElementChild.clientWidth) + "px)";
            }, 4000);
          })();
        </script>

        <div class="blog-news">
          <h3 class="blog-news-title">LATEST NEWS</h3>
          <p>&#128293; <strong>Exciting News!</strong> Our Research Accepted in RSC Materials Horizons Journal 2024-Apr-24</p>
        </div>
      </main>

    </div>
  </section>'''

if home_pattern.search(text):
    text = home_pattern.sub(NEW_HOME, text, count=1)
    print("SUCCESS: Home section replaced")
else:
    print("ERROR: Pattern not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
