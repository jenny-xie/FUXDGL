import React from 'react'
import { Navbar } from 'react-bootstrap'

export default function Header() {
    return (
        <Navbar className="navbar" bg="primary" variant="dark">
            <Navbar.Brand href="/">
            {/* <img
                alt="LOGO"
                src="/logo.svg"
                width="30"
                height="30"
                className="d-inline-block align-top"
            />{' '} */}
            Navbar
            </Navbar.Brand>
        </Navbar>
    )
}
