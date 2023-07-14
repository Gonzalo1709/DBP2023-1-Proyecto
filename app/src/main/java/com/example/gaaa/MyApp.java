package com.example.gaaa;

import android.app.Application;

public class MyApp extends Application {
    private String loggedInTrainerId;

    public String getLoggedInTrainerId() {
        return loggedInTrainerId;
    }

    public void setLoggedInTrainerId(String trainerId) {
        loggedInTrainerId = trainerId;
    }
}

