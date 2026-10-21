import { configureStore } from "@reduxjs/toolkit";
import preferencesReducer from './preferencesSlice.js';

const store = configureStore({
    reducer: {
        preferences: preferencesReducer,
    },
});

export default store;