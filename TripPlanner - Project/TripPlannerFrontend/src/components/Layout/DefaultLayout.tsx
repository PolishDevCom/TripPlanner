import React from 'react';
import { Composition } from 'atomic-layout';

interface DefaultLayoutProps extends React.ComponentProps<typeof Composition> {
  children: React.ReactNode;
}

export const DefaultLayout = ({ children, ...props }: DefaultLayoutProps) => (
  <Composition 
    width='100%'
    paddingHorizontalTabletDown={1} 
    {...props}
    >
    {children}
  </Composition>
);
