import React from 'react';
import { Composition } from 'atomic-layout';
import { Container, PoweredByVercelImg } from './Footer.styled';

export const Footer = () => (
  <Container>
    <Composition
      as="footer"
      justifyContent="end"
      alignItems="end"
      paddingHorizontal={2}
      paddingVertical={2}
      height="100%"
    >
      <a
        target="_blank"
        rel="noopener noreferrer"
        href="https://vercel.com/?utm_source=PolishDev_TripPlanner&utm_campaign=oss"
      >
        <PoweredByVercelImg />
      </a>
    </Composition>
  </Container>
);
