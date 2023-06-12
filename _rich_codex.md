# Rich-Codex

Check at each new commit:
Create a directory named codex_img.
Create .githooks dir in repo w/ a file named pre-commit containing:

```
#!/usr/bin/bash

RED='\e[1;31m'
GREEN='\e[1;32m'
BLUE='\e[1;34m'
YELLOW='\e[1;33m'
NC='\e[0m'

# If you want to allow skip of codex check set this variable to true.
allowskipcodex=$(git config --type=bool hooks.allowskipcodex)

# Redirect output to stderr.
exec 1>&2

if [ "$allowskipcodex" != "true" ];then

	python3 -c "import rich_codex"
	res=$?
	if [ $res != 0 ]; then

	echo ""
	echo -e "${RED}Error: Python module rich-codex is not installed${NC}"
	echo ""
	echo -e "Please install: ${GREEN}pip install rich-codex${NC}"
	echo ""
	echo "This is used to keep the README documentation up to date"
	echo ""
	echo "If you know what you are doing you can disable this check using:"
	echo ""
	echo -e "${BLUE}git config hooks.allowskipcodex true${NC}"
	echo ""

		exit 1
	fi
	rich-codex --skip-git-checks --no-confirm

fi


if [ "$allowskipcodex" != "true" ] && test $(git diff codex_img/ | wc -l) != 0; then

	echo ""
	echo -e "${RED}Error: Changes made to files.${NC}"

	echo ""
	echo -e "Please add and commit these changes: ${GREEN}git add .${NC}"
	echo ""
	echo -e "This must be commited to keep the ${YELLOW}README${NC} documentation up to date"
	echo ""
	echo "If you know what you are doing you can disable this check using:"
	echo ""
	echo -e "${BLUE}git config hooks.allowskipcodex true${NC}"
	echo ""

	git status
	exit 1
fi
```
In your make file, add a target:

git_hooks:
	git config --local core.hooksPath .githooks/

In the README.md for your repo you can change the following template lines to fit your needs:

<!-- RICH-CODEX
hide_command: true
terminal_width: 60
terminal_theme: SVG_EXPORT_THEME
-->
![`rich repo_directory/some_other_directory/file_to_check_4_changes.json --force-terminal --guides --panel rounded --panel-style blue`](codex_img/file_to_check_4_changes.svg)

This will create an image in your README.md that rich will create and can update whenever a commit is made.
