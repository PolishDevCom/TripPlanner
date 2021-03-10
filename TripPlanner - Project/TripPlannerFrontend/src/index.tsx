import React from 'react';
import ReactDOM from 'react-dom';
import Layout from 'atomic-layout';
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

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
import { Footer } from './components/Footer/Footer';

ReactDOM.render(
  <React.StrictMode>
    <GlobalStyle />

    <Provider store={store}>
      <Router>
        <Switch>
          {routes.map((route) => (
            <Route key={`${route.path}`} {...route} />
          ))}
        </Switch>
      </Router>

      <Footer />
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);
