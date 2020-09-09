new-problem:
	@if [ -z "$(NAME)" ]; then \
		echo "must provide the problem name NAME=the-problem"; \
		exit 1; \
	fi

	@echo "Creating the folder structure for the problem: $(NAME)"

	@mkdir $(NAME)
	@echo "insert-test-input-here" > $(NAME)/input01.txt
	@cp _templates/main.py.tpl $(NAME)/main.py
	@cp _templates/Makefile.tpl $(NAME)/Makefile
	@cp _templates/README.md.tpl $(NAME)/README.md
	@ls -l $(NAME)
.PHONY:new-problem