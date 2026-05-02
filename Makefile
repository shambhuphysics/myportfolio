# ────────────────────────────────────────────────────────────────────
#  Makefile — Shambhu's Research Portfolio
#
#  Source layout:
#    pages/      HTML source files
#    styles/     style.css + script.js
#    images/     all images (stays at root)
#    cv/         PDF (gitignored, copied into build if present)
#
#  Build output:
#    docs/       flat site ready for GitHub Pages
#                (GitHub Pages → Settings → Pages → /docs folder)
#
#  Live URL: https://shambhubhandari.github.io
# ────────────────────────────────────────────────────────────────────

REMOTE    := origin
BRANCH    := main
PORT      := 8000
LIVE      := https://shambhubhandari.github.io

SRC_PAGES := pages
SRC_STYLES := styles
OUT       := docs

.DEFAULT_GOAL := help

.PHONY: help build serve open deploy status log clean

# ── Help ─────────────────────────────────────────────────────────────
help:
	@echo ""
	@echo "  Portfolio — available targets"
	@echo "  ─────────────────────────────"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'
	@echo ""

# ── Build ─────────────────────────────────────────────────────────────
build: ## Assemble pages/ + styles/ + images/ → docs/
	@rm -rf $(OUT)
	@mkdir -p $(OUT)
	@cp $(SRC_PAGES)/*.html  $(OUT)/
	@cp $(SRC_STYLES)/style.css  $(OUT)/style.css
	@cp $(SRC_STYLES)/script.js  $(OUT)/script.js
	@cp -r images  $(OUT)/images
	@[ -d cv ] && cp -r cv $(OUT)/cv || true
	@echo "✓  Built → $(OUT)/  ($$(ls $(OUT)/*.html | wc -l | tr -d ' ') pages)"

# ── Local dev ─────────────────────────────────────────────────────────
serve: build ## Build then serve docs/ at http://localhost:$(PORT)
	@echo "→  http://localhost:$(PORT)  (Ctrl-C to stop)"
	cd $(OUT) && python3 -m http.server $(PORT)

open: ## Open the live GitHub Pages site in the browser
	xdg-open $(LIVE) 2>/dev/null || open $(LIVE) 2>/dev/null || \
		echo "Open: $(LIVE)"

# ── Deployment ────────────────────────────────────────────────────────
deploy: build ## Build, commit docs/ + source changes, push to GitHub Pages
	git add $(OUT)/ $(SRC_PAGES)/ $(SRC_STYLES)/
	git diff --cached --quiet \
		&& echo "Nothing to commit — already up to date." \
		|| git commit -m "Deploy: $$(date '+%Y-%m-%d %H:%M')"
	git push $(REMOTE) $(BRANCH)
	@echo ""
	@echo "✓  Live at $(LIVE)"

# ── Git helpers ───────────────────────────────────────────────────────
status: ## Working-tree status + last 5 commits
	@git status -s
	@echo ""
	@git log --oneline -5

log: ## Graph of last 10 commits
	git log --oneline --graph --decorate -10

# ── Housekeeping ──────────────────────────────────────────────────────
clean: ## Delete docs/ (rebuild with 'make build') and temp files
	@rm -rf $(OUT)
	@find . -not -path './.git/*' \( \
		-name ".DS_Store" -o -name "*~" -o -name "*.swp" -o -name "*.pyc" \
	\) -delete
	@echo "Clean — run 'make build' to reassemble."
