# ────────────────────────────────────────────────────────────────────
#  Makefile — Shambhu's Research Portfolio
#  Live site : https://shambhubhandari.github.io
#  Repo      : github.com/shambhubhandari/shambhubhandari.github.io
#  Deploy    : push to main → GitHub Pages serves root automatically
# ────────────────────────────────────────────────────────────────────

REMOTE := origin
BRANCH := main
PORT   := 8000
LIVE   := https://shambhubhandari.github.io

# Default target
.DEFAULT_GOAL := help

.PHONY: help serve open deploy status log clean

# ── Help ─────────────────────────────────────────────────────────────
help:
	@echo ""
	@echo "  Portfolio Makefile"
	@echo "  ──────────────────"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'
	@echo ""

# ── Local development ─────────────────────────────────────────────────
serve: ## Start a local dev server at http://localhost:$(PORT)
	@echo "→  Serving at http://localhost:$(PORT)  (Ctrl-C to stop)"
	python3 -m http.server $(PORT)

open: ## Open the live GitHub Pages site in the browser
	xdg-open $(LIVE) 2>/dev/null || open $(LIVE) 2>/dev/null || \
		echo "Open manually: $(LIVE)"

# ── Deployment ────────────────────────────────────────────────────────
deploy: ## Stage all site files, commit with timestamp, and push
	git add index.html style.css script.js
	git add *.html images/
	git diff --cached --quiet && echo "Nothing to commit." || \
		git commit -m "Deploy: $$(date '+%Y-%m-%d %H:%M')"
	git push $(REMOTE) $(BRANCH)
	@echo ""
	@echo "✓  Live at $(LIVE)"

# ── Git helpers ───────────────────────────────────────────────────────
status: ## Show working-tree status and last 5 commits
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
