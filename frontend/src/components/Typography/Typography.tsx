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

const Body = styled(TextBase)``;

export const Typography = {
  Heading,
  Subheading,
  Body,
};
