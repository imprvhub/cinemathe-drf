# Cinemathe-DRF Backend v0.1.0

**Welcome to the Cinemathe Backend Project**

**Note**
This project is an initial implementation and is currently under maintenance.

## Overview
Cinemathe is a work-in-progress project aimed at fast-tracking your entertainment picks. This initial release is an implementation of a Django Rest Framework (DRF) based backend that supports the Vue.js frontend application. The backend is designed to provide robust and scalable APIs for querying and managing movies and TV series data, with a primary focus on user authentication.

## Implementation Details
- **Framework**: Django Rest Framework (DRF)
- **Hosting**: Netlify (Frontend), DigitalOcean Spaces (Backend static files)
- **APIs Used**: TMDB, JustWatch
- **Frontend Integration**: Vue.js application deployed on Netlify

## Key Features in v0.1.0
- **Initial Setup and Configuration**: Project initialization with Django and DRF, including essential configurations and initial setup.
- **User Authentication**: Integration of user authentication mechanisms allowing users to log in, manage their profiles, and save their favorite movies and TV series.
- **Rebranding**: Refactoring to rebrand 'sonarflix' to 'cinemathe', ensuring all references and redirections are updated.
- **CORS Configuration**: Updated `cors_allowed_origins` to support Netlify deployments, ensuring cross-origin requests are handled correctly.
- **Static Files Management**: Implementation of `collectstatic` for Django admin, enabling proper management and deployment of static files.
- **Redirection Fixes**: Addressed issues with redirection post-rebranding to ensure seamless user experience.
- **Domain Updates**: Updated domains from 'netlify' to 'space' to reflect the current deployment strategy.

## Timeline
The backend development is now complete and fully integrated with the frontend.

## Demo
For a demo of the frontend application, check out the current state of Cinemathe [here](#).

## Notes
This project is currently under maintenance. For the latest updates and changes, refer to the Full Changelog.

**Full Changelog**: https://github.com/imprvhub/cinemathe-drf/commits/v0.1.0