import React from 'react'
import { Route, HashRouter, Switch } from 'react-router-dom'
import Main from './components/Main'
import ScrollToTop from './components/ScrollTop'
import SignInSide from "./components/SignInSide";
import Info from "./components/Info";

export default props => (
    <HashRouter>
      <ScrollToTop>
        <Switch>
          <Route exact path='/' component={ SignInSide } />
            <Route exact path='/main' component={ Main } />
            <Route exact path='/info' component={ Info } />
        </Switch>
      </ScrollToTop>
    </HashRouter>
  )