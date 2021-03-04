import { createSelector, createSlice } from '@reduxjs/toolkit';
import { formatDistance, add as addDate } from 'date-fns';
import { RootState } from '..';

interface MotivatorState {
  secondsEllapsed: number;
  date: number;
}

const initialState: MotivatorState = {
  secondsEllapsed: 0,
  date: new Date().getTime(),
};

export const motivatorSlice = createSlice({
  initialState,
  name: 'motivator',
  reducers: {
    incrementSecondsEllapsed: (state) => {
      state.secondsEllapsed += 1;
    },
  },
});

export const distanceBetweenDateAndSecondsEllapsedSelector = createSelector<
  RootState,
  MotivatorState['date'],
  MotivatorState['secondsEllapsed'],
  string
>(
  (state) => state.motivator.date,
  (state) => state.motivator.secondsEllapsed,
  (date, secondsEllapsed) => {
    const nextDate = addDate(date, { seconds: secondsEllapsed });

    return formatDistance(date, nextDate, { includeSeconds: true });
  }
);
