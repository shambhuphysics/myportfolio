# ────────────────────────────────────────────────────────────────────
#  Makefile — Shambhu's Research Portfolio
#
#  Layout:
#    pages/      HTML source (index.html + sub-pages)
#    styles/     style.css, script.js
#    images/     photos and section thumbnails
#    cv/         Shambhu_CV.pdf  (gitignored)
#    docs/       documentation notes (not the site output)
#    index.html  root redirect → pages/index.html
#
#  GitHub Pages: serves root of main branch
#  Live URL    : https://shambhubhandari.github.io
# ────────────────────────────────────────────────────────────────────

REMOTE := origin
BRANCH := main
PORT   := 8000
LIVE   := https://shambhubhandari.github.io

.DEFAULT_GOAL := help

.PHONY: help serve open deploy status log clean

# ── Help ─────────────────────────────────────────────────────────────
help:
	@echo ""
	@echo "  Portfolio — available targets"
	@echo "  ─────────────────────────────"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'
	@echo ""

# ── Local dev ─────────────────────────────────────────────────────────
serve: ## Serve the site locally at http://localhost:$(PORT)/pages/
	@echo "→  http://localhost:$(PORT)/pages/"
	python3 -m http.server $(PORT)

open: ## Open the live GitHub Pages site in the browser
	xdg-open $(LIVE) 2>/dev/null || open $(LIVE) 2>/dev/null || \
		echo "Open: $(LIVE)"

# ── Deployment ────────────────────────────────────────────────────────
deploy: ## Stage all site files, commit with timestamp, and push
	git add index.html pages/ styles/ images/
	git diff --cached --quiet \
		&& echo "Nothing to commit — already up to date." \
		|| git commit -m "Deploy: $$(date '+%Y-%m-%d %H:%M')"
	git push $(REMOTE) $(BRANCH)
	@echo ""
	@echo "✓  Live at $(LIVE)"

# ── Git helpers ───────────────────────────────────────────────────────
status: ## Working-tree status and last 5 commits
	@git status -s
	@echo ""
	@git log --oneline -5

log: ## Graph of last 10 commits
	git log --oneline --graph --decorate -10

# ── Housekeeping ──────────────────────────────────────────────────────
clean: ## Remove OS/editor temp files (.DS_Store, *~, *.swp, *.pyc)
	@find . -not -path './.git/*' \( \
		-name ".DS_Store" -o -name "*~" -o -name "*.swp" -o -name "*.pyc" \
	\) -delete
	@echo "Clean."
