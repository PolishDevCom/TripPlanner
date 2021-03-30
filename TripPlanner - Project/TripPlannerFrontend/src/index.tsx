import React from 'react';
import ReactDOM from 'react-dom';
import Layout from 'atomic-layout';
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { Header } from '../src/components/Layout/Header';

Layout.configure({
  defaultUnit: 'rem',
  defaultBreakpointName: 'mobile',
  breakpoints: {
    mobile: {
      maxWidth: '500px',
    },
    tablet: {
      minWidth: '501px',
      maxWidth: '764px',
    },
    desktop: {
      minWidth: '765px',
    },
  },
});

import { GlobalStyle } from './GlobalStyle';
import { store } from './store';
import { routes } from './routes';

ReactDOM.render(
  <React.StrictMode>
    <GlobalStyle />
    <Header />
    <Provider store={store}>
      <Router>
        <Switch>
          {routes.map((route) => (
            <Route key={`${route.path}`} {...route} />
          ))}
        </Switch>
      </Router>
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);
