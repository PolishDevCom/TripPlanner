import React, { useState } from 'react';
import { DefaultLayout } from './DefaultLayout';
import styled from 'styled-components';
import Logo from '../Branding/Logo';

const testUser = {
  isLogged: false,
  name: 'Bill',
  surname: 'Gates',
};

export const Header = () => {
  const [user, setUser] = useState(testUser);

  const toggleIsUserLogged = () => {
    setUser((prevState) => ({
      ...prevState,
      isLogged: !prevState.isLogged,
    }));
  };

  const Header = styled.div`
    display: flex;
    align-items: center;
    width: 100%;
    justify-content: space-between;
    & > h3 {
      padding-left: 1rem;
      font-family: Work Sans, sans-serif;
      font-style: normal;
      font-weight: 600;
      font-size: 17.4703px;
      line-height: 20px;
      letter-spacing: -0.03em;
    }
  `;

  const Nav = styled.ul`
    width: 50%;
    display: flex;
    list-style-type: none;
    justify-content: flex-end;
    font-family: Work Sans, sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 13px;
    line-height: 15px;
    color: #919191;
  `;

  const MenuList = styled.li`
    padding-right: 1rem;
  `;

  return (
    <DefaultLayout onClick={toggleIsUserLogged} style={{ padding: '0' }}>
      <Header>
        <Logo></Logo>
        <Nav>
          <MenuList>Explore</MenuList>
          {user.isLogged ? (
            <MenuList>
              Hello, {user.name} {user.surname}
            </MenuList>
          ) : (
            <MenuList>Create account</MenuList>
          )}
        </Nav>
      </Header>
    </DefaultLayout>
  );
};
