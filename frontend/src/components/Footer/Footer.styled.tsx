import styled from 'styled-components';

export const Container = styled.div`
  height: 100px;
  margin-top: 100px;
  background: #eee;
`;

export const PoweredByVercelImg = styled.img.attrs((props) => ({
  ...props,
  src: '/powered-by-vercel.svg',
  alt: 'Powered by Vercel',
}))`
  height: 30px;
`;
