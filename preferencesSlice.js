import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    weatherSensitivityOption: ['Heat sensitive', 'Cold sensitive', 'Rain sensitive', 'Wind sensitive', 'UV sensitive'],
    commuteType: "",
    weatherSensitivity: "",
    dailyActivity: "",
    responseStyle: "",
};

const preferencesSlice = createSlice({
    name: "preferences",
    initialState,
    reducers: {
        setWeatherSensitivityOption: (state, action) => {
            state.weatherSensitivityOption.push(action.payload);
        },
        setWeatherSensitivity: (state, action) => {
            state.weatherSensitivity = action.payload;
        },
        setCommuteType: (state, action) => {
            state.commuteType = action.payload;
        },
        setDailyActivity: (state, action) => {
            state.dailyActivity = action.payload;
        },
        setResponseStyle: (state, action) => {
            state.responseStyle = action.payload;
        },
        resetPreferences: () => initialState,
    }
})

export const {
  setWeatherSensitivityOption,
  setWeatherSensitivity,
  setCommuteType,
  setDailyActivity,
  setResponseStyle,
  resetPreferences,
} = preferencesSlice.actions;

export default preferencesSlice.reducer;