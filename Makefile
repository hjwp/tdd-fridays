test:
	pytest

watch-tests:
	git ls-files | entr pytest

commit:
	git add . && git commit -m"another commit" && git push

