package com.example.fasal;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class Language extends AppCompat {

    private Button english,hindi,tamil,kannada,malayalam;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_language);

        english=findViewById(R.id.eng);
        hindi=findViewById(R.id.hindi);
        tamil=findViewById(R.id.tamil);
        kannada=findViewById(R.id.kannada);

        LanguageManager lang=new LanguageManager(this);

        english.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                lang.updateResource("en");
                findViewById(R.id.en);
                recreate();
                nextActivity();
            }
        });

        hindi.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                lang.updateResource("hi");
                recreate();
                nextActivity();
            }
        });

        tamil.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                lang.updateResource("ta");
                findViewById(R.id.ta);
                recreate();
                nextActivity();
            }
        });

        kannada.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                lang.updateResource("kn");
                findViewById(R.id.kn);
                recreate();
                nextActivity();
            }
        });

    }

    public void nextActivity()
    {
        Intent intent=new Intent(Language.this,MainActivity.class);
        startActivity(intent);
    }


}