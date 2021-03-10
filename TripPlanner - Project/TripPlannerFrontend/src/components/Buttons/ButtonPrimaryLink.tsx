import styled from 'styled-components'

const ButtonLink = styled.button`
  padding: 10px 18px 10px 18px;
  width: 105px;
  height: 34px;
  background-color: transparent;
  border: 0;
  border-radius: 6px;
  color: #F53314;
  cursor: pointer;
  left: calc(50% - 105px/2);
  top: calc(50% - 34px/2 + 54px);
  font-family: Work Sans, sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 12px;
  line-height: 14px;
  
  &:hover {
    color: #F75D45;
  }
  &:disabled {
    color: #ADADAD;
  }
  &:active {
    color: #F98876;
  }
  &:focus {
    border: 2px solid #FBB2A7;
    padding: 0;
  }
`
export default ButtonLink;
