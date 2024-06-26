import React from 'react';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import MainPage from './components/Pages/MainPage';
import LogoutForm from './components/Forms/LogoutForm';
import RegistrationForm from './components/Forms/RegistrationForm';
import LoginForm from './components/Forms/LoginForm';
import UserProfile from "./components/Pages/UserProfile";
import Specialists from "./components/Pages/Specialists";
import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";
import SpecialistProfile from "./components/Pages/SpecialistProfile";
import SpecInfo from "./components/Pages/SpecInfo";


function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={(
                    <div>
                        <MainPage></MainPage>
                    </div>
                )}>
                </Route>
                <Route path="/profile" element={(
                    <div>
                        <Header></Header>
                        <div className="mt-4"></div>
                        <UserProfile></UserProfile>
                        <Footer></Footer>
                    </div>
                )}>
                </Route>
                <Route path="/spec-profile" element={(
                    <div>
                        <Header></Header>
                        <div className="mt-4"></div>
                        <SpecInfo></SpecInfo>
                        <Footer></Footer>
                    </div>
                )}>
                </Route>
                <Route path="/specialists" element={(
                    <div>
                        <Header></Header>
                        <div className="mt-4"></div>
                        <Specialists></Specialists>
                        <Footer></Footer>
                    </div>
                )}>
                </Route>
                <Route path="/specialist">
                    <Route path=":id" element={(
                        <div>
                            <Header></Header>
                            <div className="mt-4"></div>
                            <SpecialistProfile></SpecialistProfile>
                            <Footer></Footer>
                        </div>
                    )}>
                    </Route>
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
