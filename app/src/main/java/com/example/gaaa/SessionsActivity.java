package com.example.gaaa;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.Toast;

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

public class SessionsActivity extends AppCompatActivity {

    private RequestQueue queue;
    private ArrayAdapter<String> sessionListAdapter;
    private List<String> sessionList;
    private String loggedInTrainerId;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Log.d("SessionsActivity", "loggedInTrainerId: " + loggedInTrainerId);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sessions);

        Button refreshButton = findViewById(R.id.refreshButton2);
        ListView sessionListView = findViewById(R.id.sessionListView);

        queue = Volley.newRequestQueue(this);

        sessionList = new ArrayList<>();
        sessionListAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, sessionList);
        sessionListView.setAdapter(sessionListAdapter);

        refreshButton.setOnClickListener(v -> obtenerDatosVolley());

        Intent intent = getIntent();
        if (intent != null && intent.hasExtra("loggedInTrainerId")) {
            loggedInTrainerId = intent.getStringExtra("loggedInTrainerId");
        } else {
            Toast.makeText(this, "Trainer ID not available", Toast.LENGTH_SHORT).show();
            finish();
        }

        obtenerDatosVolley();
    }

    private void obtenerDatosVolley() {
        String url = "https://zergixz.pythonanywhere.com/sessions";

        Log.d("SessionsActivity", "Making request to: " + url);

        JsonArrayRequest request = new JsonArrayRequest(Request.Method.GET, url, null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        sessionList.clear();
                        try {
                            for (int i = 0; i < response.length(); i++) {
                                JSONObject session = response.getJSONObject(i);
                                int entrenadorId = session.getInt("entrenador_id");
                                if (entrenadorId == Integer.parseInt(loggedInTrainerId)) {
                                    int usuarioId = session.getInt("usuario_id");
                                    String fecha = session.getString("fecha");
                                    int precio = session.getInt("precio");
                                    sessionList.add("Usuario ID: " + usuarioId + "\nFecha: " + fecha + "\nPrecio: " + precio);
                                }
                            }
                            sessionListAdapter.notifyDataSetChanged();
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(SessionsActivity.this, "Error retrieving sessions", Toast.LENGTH_SHORT).show();
                    }
                });

        queue.add(request);
    }
}
