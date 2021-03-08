import React from 'react';

export const useInterval = (callback: () => unknown, delay: number) => {
  const timeoutRef = React.useRef<number | undefined>();
  const callbackRef = React.useRef(callback);

  React.useEffect(() => {
    callbackRef.current = callback;
  }, [callback]);

  React.useEffect(() => {
    timeoutRef.current = window.setInterval(() => callbackRef.current(), delay);

    return () => window.clearInterval(timeoutRef.current);
  }, [delay]);

  return timeoutRef;
};
