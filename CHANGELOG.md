# Changelog

All notable changes to the project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).





## [0.3.2] - 2025-05-24

### Added
- 

### Changed
- release yaml file

### Fixed
- versioning workflow

## [0.3.1] - 2025-05-24

### Added
- 

### Changed
- 

### Fixed
- pypi integration

## [0.3.0] - 2024-07-08

### Added
- Comprehensive unit and integration testing framework
- Robust environment-specific configuration system
- Docker containerization with multi-stage builds
- Development, testing, production, and Docker-specific configurations
- Automated utility scripts for setup, testing, and deployment
- Quality assurance tooling with pre-commit hooks
- Advanced CI/CD workflows for unit tests, integration tests, and linting
- Type checking with mypy integration
- Security scanning with bandit
- Improved package management with modern Python standards
- Enhanced project metadata and classifiers
- Support for Python 3.9, 3.10 and 3.12 
- Redis-based caching for production environments
- Proper health checks for Docker containers
- Rate limiting and CORS configuration for API
- JSON-formatted structured logging
- Comprehensive test coverage for all core services
- Test parameterization for multiple scenarios

### Changed
- Upgraded packaging configuration to follow modern Python standards
- Updated requirements management with environment-specific files
- Improved CI/CD workflows with separate unit and integration test jobs
- Enhanced Docker configuration with security best practices
- Better test organization with separate unit and integration tests
- Non-root user execution in Docker containers
- More granular control over testing with command-line options
- Updated project documentation to reflect new architecture
- Improved dependency management with proper extras_require
- Configuration system now supports multiple environments

### Fixed
- Dependency resolution issues in package setup
- Test isolation and independence
- Docker build performance with multi-stage approach
- Security issues with Docker configuration
- Environment-specific configuration loading
- Build system compatibility
- Package distribution completeness
- Type checking coverage

## [0.2.0] - 2024-07-01

### Added
- Service-oriented architecture implementation
- New API access via FastAPI
- Core business logic extracted to independent services
- Comprehensive models and DTOs for data validation
- Proper separation between CLI, API, and core functionality
- API Endpoints for all existing CLI functionality
- Improved error handling with custom exceptions
- Structured directory layout for better maintainability
- Support for both CLI and HTTP API from the same codebase
- Docker configuration for API and CLI deployment
- API documentation with Swagger/OpenAPI
- Enhanced visualization capabilities for comparison data
- Improved export options with structured JSON output

### Changed
- Moved from monolithic structure to layered architecture
- Refactored CLI commands to use service layer
- Updated packaging configuration for multiple distribution types
- Improved configuration management
- Enhanced test organization
- Better handling of complex data models for export
- More consistent interface between CLI and API components

### Fixed
- Improved error handling with consistent patterns
- Better handling of API rate limits
- Structured exception hierarchy
- Fixed issues with exporting comparison data
- Resolved visualization compatibility problems
- Fixed data serialization for complex nested models

## [0.1.3] - 2025-05-02

### Added
- 

### Changed
- 

### Fixed
- README typo updated

## [0.1.2] - 2025-05-02

### Added
- Initial release of Google Trends CLI tool
- Command-line interface for accessing Google Trends data
- Core commands: `trending`, `related`, `compare`, `suggest-topics`, `writing-opportunities`
- Support for content creator recommendations and topic suggestions
- Geographic interest analysis with configurable resolution
- Multiple export formats (CSV, JSON, Excel)
- Independent time-series analysis for multiple keywords
- Visualization support for trend data
- Comprehensive documentation and examples
- Integration with TrendsPy for improved API reliability

### Changed
- First public release patched

### Fixed
- Initial stable implementation patched tho.

## [0.1.1] - 2025-05-02

### Added
- Initial release of Google Trends CLI tool
- Command-line interface for accessing Google Trends data
- Core commands: `trending`, `related`, `compare`, `suggest-topics`, `writing-opportunities`
- Support for content creator recommendations and topic suggestions
- Geographic interest analysis with configurable resolution
- Multiple export formats (CSV, JSON, Excel)
- Independent time-series analysis for multiple keywords
- Visualization support for trend data
- Comprehensive documentation and examples
- Integration with TrendsPy for improved API reliability

### Changed
- First public release patched

### Fixed
- Initial stable implementation.


## [0.1.0] - 2023-05-20

### Added
- Initial release of Google Trends CLI tool
- Command-line interface for accessing Google Trends data
- Core commands: `trending`, `related`, `compare`, `suggest-topics`, `writing-opportunities`
- Support for content creator recommendations and topic suggestions
- Geographic interest analysis with configurable resolution
- Multiple export formats (CSV, JSON, Excel)
- Independent time-series analysis for multiple keywords
- Visualization support for trend data
- Comprehensive documentation and examples
- Integration with TrendsPy for improved API reliability

### Changed
- First public release

### Fixed
- Initial stable implementation.
