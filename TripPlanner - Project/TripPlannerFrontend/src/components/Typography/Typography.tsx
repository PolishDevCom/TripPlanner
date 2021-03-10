import styled from 'styled-components';

/**
 * Font sizes are in minor third scale.
 * @see https://type-scale.com/
 */

const TextBase = styled.p`
  margin: 0;
  padding: 0;

  line-height: 1.5;
`;

const Heading = styled(TextBase)`
  font-size: 2.488rem;
`;

const Subheading = styled(TextBase)`
  font-size: 2.074rem;
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
  & > li {
    padding-right: 1rem;
  }
`;

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

const Body = styled(TextBase)``;

export const Typography = {
  Heading,
  Subheading,
  Body,
  Nav,
  Header
};
