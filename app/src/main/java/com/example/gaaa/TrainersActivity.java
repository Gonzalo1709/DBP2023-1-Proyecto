// TrainersActivity.java

package com.example.gaaa;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;

import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class TrainersActivity extends AppCompatActivity {

    private RequestQueue queue;
    private ArrayAdapter<String> userListAdapter;
    private List<String> userList;
    public static final String EXTRA_TRAINER_ID = "loggedInTrainerId";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_trainers);

        Button refreshButton = findViewById(R.id.refreshButton);
        ListView userListView = findViewById(R.id.userListView);
        Button sessionsButton = findViewById(R.id.sessionsButton);

        queue = Volley.newRequestQueue(this);

        userList = new ArrayList<>();
        userListAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, userList);
        userListView.setAdapter(userListAdapter);

        sessionsButton.setOnClickListener(v -> {
            Intent intent = getIntent();
            if (intent != null && intent.hasExtra("loggedInTrainerId")) {
                String loggedInTrainerId = intent.getStringExtra("loggedInTrainerId");
                Log.d("TrainersActivity", "loggedInTrainerId: " + loggedInTrainerId);

                Intent sessionsIntent = new Intent(TrainersActivity.this, SessionsActivity.class);
                sessionsIntent.putExtra("loggedInTrainerId", loggedInTrainerId);
                startActivity(sessionsIntent);
            }
        });

        refreshButton.setOnClickListener(v -> obtenerDatosVolley());
        obtenerDatosVolley();
    }

    private void obtenerDatosVolley() {
        String url = "https://zergixz.pythonanywhere.com/users";

        Log.d("TrainersActivity", "Making request to: " + url);

        JsonArrayRequest request = new JsonArrayRequest(Request.Method.GET, url, null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        userList.clear();
                        try {
                            for (int i = 0; i < response.length(); i++) {
                                JSONObject user = response.getJSONObject(i);
                                String email = user.getString("email");
                                String password = user.getString("password");
                                userList.add("Email: " + email + "\nPassword: " + password);
                            }
                            userListAdapter.notifyDataSetChanged();
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.e("TrainersActivity", "Error: " + error.toString());
                    }
                });

        queue.add(request);
    }
}
