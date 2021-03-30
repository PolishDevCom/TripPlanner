import styled from 'styled-components';

export const ButtonPrimary = styled.button`
  padding: 10px 18px 10px 18px;
  width: 105px;
  height: 34px;
  background-color: #f53314;
  border: 0;
  border-radius: 6px;
  color: #fff;
  font-style: normal;s
  font-weight: 500;
  font-size: 12px;
  line-height: 14px;

  &:hover {
    background: #f75d45;
  }
  &:disabled {
    background: #d1d1d1;
    color: #adadad;
  }
  &:active {
    background: #f98876;
  }
  &:focus {
    border: 2px solid #fbb2a7;
    padding: 0;
  }
`;
