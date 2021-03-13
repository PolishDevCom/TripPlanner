import React from 'react';
import { Composition } from 'atomic-layout';

interface DefaultLayoutProps extends React.ComponentProps<typeof Composition> {
  children: React.ReactNode;
}

export const DefaultLayout = ({ children, ...props }: DefaultLayoutProps) => (
  <Composition maxWidth="640px" paddingHorizontalTabletDown={1} {...props}>
    {children}
  </Composition>
);
