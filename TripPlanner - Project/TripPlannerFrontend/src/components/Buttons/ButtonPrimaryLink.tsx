import styled from 'styled-components';

export const ButtonLink = styled.button`
  padding: 10px 18px 10px 18px;
  width: 105px;
  height: 34px;
  background-color: transparent;
  border: 0;
  border-radius: 6px;
  color: #f53314;
  font-style: normal;
  font-weight: 500;
  font-size: 12px;
  line-height: 14px;

  &:hover {
    color: #f75d45;
  }
  &:disabled {
    color: #adadad;
  }
  &:active {
    color: #f98876;
  }
  &:focus {
    border: 2px solid #fbb2a7;
    padding: 0;
  }
`;
