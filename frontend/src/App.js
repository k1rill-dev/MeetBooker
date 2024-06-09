import React from 'react';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import MainPage from './components/Pages/MainPage';
import LogoutForm from './components/Forms/LogoutForm';
import RegistrationForm from './components/Forms/RegistrationForm';
import LoginForm from './components/Forms/LoginForm';


function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={(
                    <div>
                        {/*<Header></Header>*/}
                        {/*<div className="mt-4"></div>*/}
                        <MainPage></MainPage>
                        {/*<Footer></Footer>*/}
                    </div>
                )}>
                </Route>
                <Route path="/logout" element={(
                    <div>
                        <LogoutForm></LogoutForm>
                    </div>
                )}>
                </Route>
                <Route path="/register" element={(
                    <div>
                        <RegistrationForm></RegistrationForm>
                    </div>
                )}>
                </Route>
                <Route path="/login" element={(
                    <div>
                        <LoginForm></LoginForm>
                    </div>
                )}>
                </Route>
            </Routes>
        </BrowserRouter>
    );
}

export default App;
