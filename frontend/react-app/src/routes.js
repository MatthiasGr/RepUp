import React from 'react'
import { Route, HashRouter, Switch } from 'react-router-dom'
import Dashboard from './components/Dashboard'
import Wizard from './components/Wizard'
import Cards from './components/Cards'
import Main from './components/Main'
import Signup from './components/Signup'
import ScrollToTop from './components/ScrollTop'
import SignInSide from "./components/SignInSide";

export default props => (
    <HashRouter>
      <ScrollToTop>
        <Switch>
          <Route exact path='/' component={ SignInSide } />
            <Route exact path='/main' component={ Main } />
        </Switch>
      </ScrollToTop>
    </HashRouter>
  )