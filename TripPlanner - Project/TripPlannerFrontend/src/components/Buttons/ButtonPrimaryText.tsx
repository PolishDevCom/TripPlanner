import styled from 'styled-components';

export const ButtonText = styled.button`
  padding: 10px 18px;
  width: 105px;
  height: 34px;
  background-color: #fff;
  border: 1px solid #f53314;
  border-radius: 6px;
  color: #f53314;
  font-style: normal;
  font-weight: 500;
  font-size: 12px;
  line-height: 14px;

  &:hover {
    border: 1px solid #f75d45;
    color: #f75d45;
  }
  &:disabled {
    border: 1px solid #adadad;
    color: #adadad;
  }
  &:active {
    border: 1px solid #f98876;
    color: #f98876;
  }
  &:focus {
    border: 2px solid #fbb2a7;
    padding: 9px 18px 10px 18px;
  }
`;
