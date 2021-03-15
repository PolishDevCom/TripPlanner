import { configureStore } from '@reduxjs/toolkit';
import { motivatorSlice } from './motivator/motivatorSlice';

export const store = configureStore({
  reducer: {
    motivator: motivatorSlice.reducer,
  },
  devTools: {
    trace: true,
    shouldCatchErrors: true,
  },
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
