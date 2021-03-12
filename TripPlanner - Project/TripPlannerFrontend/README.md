![](public/og.png 'Title')

[![](public/powered-by-vercel.svg 'Powered by Vercel')](https://vercel.com/?utm_source=PolishDev_TripPlanner&utm_campaign=oss)

# TripPlanner Frontend

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Node.js](https://nodejs.org/en/) - latest LTS or current version
- [yarn](https://classic.yarnpkg.com/en/docs/install/) - latest version

#### Node.js version

In [prerequisites](#prerequisites) there's a statement recommending

> latest LTS or current version of node.js

If for whatever reason your development environment is acting strange (dev server not starting, something's off, etc.), please ensure you're using the version of node.js specified in [.nvmrc](.nvmrc). If you have [nvm](https://github.com/nvm-sh/nvm) installed, all you have to do is to run `nvm use` while in `TripPlanner - Project/TripPlannerFrontend`. `nvm use` will install and use version of node.js specified in `.nvmrc`.

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

Running the `build` task will create a production-ready version of the app.

```sh
yarn build
```

#### Serving the build

Running the `serve` task will serve built app.

```sh
yarn serve
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
