![](public/og.png 'Title')

# TripPlanner Frontend

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Node.js](https://nodejs.org/en/) - latest LTS or current version
- [yarn](https://classic.yarnpkg.com/en/docs/install/) - latest version

### Installing

1. Clone the repo:

```sh
git clone git@github.com:UgzSourceCode/TripPlanner.git
```

2. Go to TripPlannerFrontend:

```sh
cd TripPlanner\ -\ Project/TripPlannerFrontend
```

3. Install dependencies:

```sh
yarn
```

tl;dr

```sh
git clone git@github.com:UgzSourceCode/TripPlanner.git &&\
cd TripPlanner/TripPlanner\ -\ Project/TripPlannerFrontend &&\
yarn
```

### Development

Running the `dev` task will start a development server on `localhost:3000`.

Dev server support hot-reloading and auto refreshing, so you don't need to worry about hitting refresh on every change made.

```sh
yarn dev
```

### Building

Running the `build` task will create a production-ready version of website.

```sh
yarn build
```

### Linting, formatting

To run linting:

```sh
yarn lint
```

To run linting and fix potential issues:

```sh
yarn lint:fix
```

To run formatting:

```sh
yarn format
```

To run formatting and fix potential issues:

```sh
yarn format:fix
```

## Built With

- [TypeScript](https://www.typescriptlang.org/)
- [Vite](https://vitejs.dev/) - tooling
- [React](https://reactjs.org/) - building UI
- [Redux](https://redux.js.org/) - global state
- [styled components](https://styled-components.com/) - styling UI

...and more! See [package.json](package.json) for used packages.
