import styled from 'styled-components'

const ButtonText = styled.button`
  padding: 10px 18px;
  width: 105px;
  height: 34px;
  background-color: #fff;
  border: 1px solid #F53314;
  border-radius: 6px;
  color: #F53314;
  cursor: pointer;
  left: calc(50% - 105px/2);
  top: calc(50% - 34px/2 + 54px);
  
  &:hover {
    border: 1px solid #F75D45;
    color: #F75D45;
  } 
  &:disabled {
    border: 1px solid #ADADAD;
    color: #ADADAD;
  } 
  &:active {
    border: 1px solid #F98876;
    color: #F98876;
  }
  &:focus {
    border: 2px solid #FBB2A7;
    padding: 9px 18px 10px 18px;
  }
`
export default ButtonText;
