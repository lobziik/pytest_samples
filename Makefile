.PHONY: help


help: ## prints help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


dates_and_times: ## freezegun sample
	@pytest freezegun_sample


http: ## httmock sample
	@pytest http_mock


fixtures: ## simple_fixtures sample
	@pytest simple_fixtures


setup_and_teardown: ## yield_fixtures_and_scopes sample
	@pytest yield_fixtures_and_scopes


parametrize: ## parametrize_value_expected sample
	@pytest parametrize_value_expected


marking_tests: ## excluding marked test sample
	@pytest marks -m "not other_mark"


marking_module: ## excluding marked module sample
	@pytest marks -m "not whole_module"


mocking: ## mocking sample
	@pytest mocks


pytest_onplace_debug: ## run pytest with pudb
	@pytest onplace_debugging --capture=no # capture disabling matter for pudb


onplace_debug: ## on place debugging sample
	python onplace_debugging
