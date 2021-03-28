import React from 'react'
import { Navbar } from 'react-bootstrap'
import './Header.css'
import logo from './SASEHACKS_LOGO.png'

export default function Header() {
    return (
        <Navbar style={{textAlign: "center"}} className="navbar-header" bg="primary" variant="dark">
            {/* <Navbar.Brand href="/"> */}
            <img
                alt="LOGO"
                src = {logo}
                width="30"
                height="30"
                className="d-inline-block align-top"
            />{' '}
            <div class="navbar-header">
                
                <a class="navbar-brand" href="#">Transcript Parser</a>
            </div>
            
            {/* </Navbar.Brand> */}
        </Navbar>
    )
}
