package com.example.gaaa;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkError;
import com.android.volley.NoConnectionError;
import com.android.volley.Request;
import com.android.volley.ServerError;
import com.android.volley.TimeoutError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;
import org.json.JSONException;
import org.json.JSONObject;

public class LoginActivity extends AppCompatActivity {

 private EditText emailEditText;
 private EditText passwordEditText;
 private static final String URL = "https://zergixz.pythonanywhere.com/trainers";

 @Override
 protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  setContentView(R.layout.activity_login);

  emailEditText = findViewById(R.id.editTextTextPersonName);
  passwordEditText = findViewById(R.id.editTextTextPassword);
  Button loginButton = findViewById(R.id.loginBtn);

  loginButton.setOnClickListener(v -> {
   String email = emailEditText.getText().toString();
   String password = passwordEditText.getText().toString();

   JsonArrayRequest request = new JsonArrayRequest(Request.Method.GET, URL, null,
           response -> {
            try {
             boolean isValidTrainer = false;
             String trainerId = "";

             for (int i = 0; i < response.length(); i++) {
              JSONObject trainerObject = response.getJSONObject(i);
              String trainerEmail = trainerObject.getString("email");
              String trainerPassword = trainerObject.getString("password");
              String id = trainerObject.getString("id");

              if (email.equals(trainerEmail) && password.equals(trainerPassword)) {
               isValidTrainer = true;
               trainerId = id;
               break;
              }
             }

             if (isValidTrainer) {
              Intent intent = new Intent(LoginActivity.this, TrainersActivity.class);
              intent.putExtra("loggedInTrainerId", trainerId);
              startActivity(intent);
             } else {
              Toast.makeText(LoginActivity.this, "Invalid credentials", Toast.LENGTH_SHORT).show();
             }
            } catch (JSONException e) {
             e.printStackTrace();
             Toast.makeText(LoginActivity.this, "Error parsing JSON", Toast.LENGTH_SHORT).show();
            }
           },
           error -> {
            String errorMessage = "Error fetching trainers data";
            if (error instanceof NoConnectionError) {
             errorMessage = "No internet connection";
            } else if (error instanceof TimeoutError) {
             errorMessage = "Request timed out";
            } else if (error instanceof AuthFailureError) {
             errorMessage = "Authentication failure";
            } else if (error instanceof ServerError) {
             errorMessage = "Server error";
            } else if (error instanceof NetworkError) {
             errorMessage = "Network error";
            }

            Log.e("LoginActivity", "Error: " + error.toString());
            Toast.makeText(LoginActivity.this, errorMessage, Toast.LENGTH_SHORT).show();
           });

   Volley.newRequestQueue(LoginActivity.this).add(request);
  });
 }
}
