import React from 'react'
import { Navbar } from 'react-bootstrap'
import './Header.css'

export default function Header() {
    return (
        <Navbar style={{textAlign: "center"}} className="navbar-header" bg="primary" variant="dark">
            {/* <Navbar.Brand href="/"> */}
            <div class="navbar-header">
                <a class="navbar-brand" href="#">Transcript Parser</a>
            </div>
            {/* <img
                alt="LOGO"
                src="/logo.svg"
                width="30"
                height="30"
                className="d-inline-block align-top"
            />{' '} */}
            {/* </Navbar.Brand> */}
        </Navbar>
    )
}
