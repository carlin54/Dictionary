-----------------------------------------------------------------------------
--
-- Module      :  Main
-- Copyright   :
-- License     :  AllRightsReserved
--
-- Maintainer  :
-- Stability   :
-- Portability :
--
-- |
--
-----------------------------------------------------------------------------

module Main (
    main
) where

import Network.HTTP.Conduit

-- Noun, Pronoun, Verb, Adjective
-- Adverb, Preposition, Conjunction, Interjection

-- Sets
-- -- Words
-- -- Word Repository
-- -- Tags
-- -- Part Of Speech |ID| ? Dynamic Sizing
-- -- Referece |ID|ID| assumed |ID|
   -- -- |Word ID|Sub Number|

-- Word
-- -- ID
-- -- String
-- -- Type Definitions (Parts of Speech)
   -- -- Noun
      -- -- Part Of Speech |ID|
      -- -- Number
      -- -- Plural
      -- -- Broad Definitions
         -- -- Tags                 |ID|
         -- -- Sub Number
         -- -- Simple Definition
         -- -- Synonyms             |ID|
         -- -- Antononyms           |ID|
         -- -- Example
   -- -- Pronoun
      -- -- Part Of Speech |ID|
      -- -- Number
      -- -- Broad Definitions
         -- -- Tags                 |ID|
         -- -- Sub Number
         -- -- Simple Definition
         -- -- Synonyms             |ID|
         -- -- Antononyms           |ID|
         -- -- Example
   -- -- Verb
      -- -- Part Of Speech |ID|
      -- -- Number
      -- -- Broad Definitions
         -- -- Tags                 |ID|
         -- -- Sub Number
         -- -- Simple Definition
         -- -- Synonyms             |ID|
         -- -- Antononyms           |ID|
         -- -- Example
      -- -- Tenses
         -- -- Verb
         -- -- 3rd Person Present
         -- -- Past Tense
         -- -- Past Participle
         -- -- Present Participle
   -- -- Adjective
      -- -- Part Of Speech |ID|
      -- -- Number
      -- -- Forms
         -- -- Adjective            |ID|
         -- -- Comparative adjective
         -- -- Superlative adjective
      -- -- Broad Definitions
         -- -- Tags                 |ID|
         -- -- Sub Number
         -- -- Simple Definition
         -- -- Synonyms             |ID|
         -- -- Antononyms           |ID|
         -- -- Example
   -- -- Adverb
      -- -- Part Of Speech |ID|
      -- -- Number
      -- -- Broad Definitions
         -- -- Tags                 |ID|
         -- -- Sub Number
         -- -- Simple Definition
         -- -- Synonyms             |ID|
         -- -- Antononyms           |ID|
         -- -- Example
   -- -- Preposition
      -- -- Part Of Speech |ID|
      -- -- Number
      -- -- Broad Definitions
         -- -- Tags                 |ID|
         -- -- Sub Number
         -- -- Simple Definition
         -- -- Synonyms             |ID|
         -- -- Antononyms           |ID|
         -- -- Example
   -- -- Conjunction
      -- -- Part Of Speech |ID|
      -- -- Number
      -- -- Broad Definitions
         -- -- Tags                 |ID|
         -- -- Sub Number
         -- -- Simple Definition
         -- -- Synonyms             |ID|
         -- -- Antononyms           |ID|
         -- -- Example
   -- -- Exclamation
      -- -- Part Of Speech |ID|
      -- -- Number
      -- -- Broad Definitions
         -- -- Tags                 |ID|
         -- -- Sub Number
         -- -- Simple Definition
         -- -- Synonyms             |ID|
         -- -- Antononyms           |ID|
         -- -- Example

data BroadDefinition = BroadDefinition {
    tags                :: [String] ,
    subNumber           :: Int      ,
    simpleDefinition    :: String   ,
    synonyms            :: [String] ,
    antonyms            :: [String] ,
    example             :: String
}

data AdjectiveForms = AdjectiveForms {
    adjective       :: String,
    comparative     :: String,
    superlative     :: String
}

data VerbTenses = Tenses {
    simplePresent               :: String,
    presentPerfect              :: String,
    presentContinuous           :: String,
    presentPerfectContinuous    :: String,
    simplePast                  :: String,
    pastPerfect                 :: String,
    pastContinuous              :: String,
    pastPerfectContinuous       :: String,
    simpleFuture                :: String,
    futurePerfect               :: String,
    futureContinuous            :: String,
    futurePerfectContinuous     :: String
}

data Noun           = Noun
data Pronoun        = Pronoun
data Verb           = Verb
data Adjective      = Adjective
data Adverb         = Adverb
data Preposition    = Preposition
data Conjunction    = Conjunction
data Exclamation    = Exclamation
data Word = Word {
    id :: Int,
    word :: String,
    nouns :: [Noun],
    pronouns :: [Pronoun],
    verbs :: [Verb],
    adjectives :: [Adjective],
    adverbs :: [Adverb],
    presuppositions :: [Preposition],
    conjunctions :: [Conjunction],
    exclamations :: [Exclamation]
}

class PartOfSpeech p where
    partOfSpeech :: p -> String
    id :: p -> Int
    definition :: p -> BroadDefinition


-- data Noun = Noun Int String BroadDefinition
-- instance PartOfSpeech Noun where
--     partOfSpeech (Noun id plural broadDefinition) = "Noun"
--     id (Noun id plural broadDefinition) = id
--     definition (Noun id plural broadDefinition) = broadDefinition


main :: IO ()
main = putStrLn "Hello, World!"
