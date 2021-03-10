import React, { useState } from 'react';
import { DefaultLayout } from './DefaultLayout';
import { Typography } from '../Typography/Typography';
import Logo from '../Branding/Logo';

const testUser = {
  isLogged: false,
  name: 'Bill',
  surname: 'Gates',
};

export default function Header() {
  const [users, setUsers] = useState(testUser);

  function changeLogin() {
    if (users.isLogged === false) {
      setUsers((prevState) => ({
        ...prevState,
        isLogged: true,
      }));
    } else {
      setUsers((prevState) => ({
        ...prevState,
        isLogged: false,
      }));
    }
  }

  return (
    <DefaultLayout onClick={changeLogin} style={{padding: "0"}}>
      <Typography.Header >
        <Logo></Logo>
        <Typography.Nav>
          <li>Explore</li>
          {users.isLogged ? (
            <li>
              Hello, {users.name} {users.surname}
            </li>
          ) : (
            <li>Create account</li>
          )}
        </Typography.Nav>
      </Typography.Header>
    </DefaultLayout>
  );
}
