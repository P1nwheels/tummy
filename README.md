# What is tummy?


tummy is a collection of all the useful CLI tools I've made for myself that I
wanted to have all in one place. Now they are (:

***

### Commands:

    tummy weather
        Subcommands:
            
            1. config LATITUDE LONGITUDE UNITS

            Allowed units include: standard, imperial, metric.
            
            Example:
                tummy weather config 38.89511, -77.03637 standard
            

    tummy notes
        Subcommands:

            1. add NOTE

            Example:
                tummy notes add "Adding a note" works with and without quotes.

            Does exactly what the name suggests.

            2. remove NUMBER

            Example:
                tummy notes remove 1

            Does exactly what the name suggests.

            3. clear

            When you use this command you will be prompted to verify that you
            are actually sure you'd like to clear your notes.

            Example:
                tummy notes clear

            Does exactly what the name suggests.

            4. show

            Does exactly what the name suggests.

            Example:
                tummy notes show


    tummy reg
        Subcommands:

            1. search LINK "REGULAR EXPRESSION" INCLUDE_EXTRA

            Example:
                tummy reg search https://theprogrammershangout.com/rules/ "\d\. [ -/:-~]+" yes

            Searches the provided link's text for all the matches of the
            regular expression that was provided. If INCLUDE_EXTRA is "yes"
            then it will pad the regex with ".{,50}" on both ends. Otherwise
            it doesn't do any extra padding.


    tummy help