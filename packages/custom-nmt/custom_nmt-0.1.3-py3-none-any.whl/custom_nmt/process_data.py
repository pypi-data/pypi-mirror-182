from ._exceptions import InvalidDatasetError
from random import shuffle
from typing import Optional
import numpy as np
from .constants import START_TOKEN, END_TOKEN, OOV_TOKEN, PAD_TOKEN
# import sentencepiece as spm
import tensorflow as tf
import keras_nlp
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
import re

def read_data_file(filename: str) -> list[str]:
    """ Reads data from a file, structured as one data point per line.
    
    Parameters:
        filename: The name of the file to load
    
    Returns:
        A list of datapoints, with newline characters stripped. No other
        processing is done here.
    """
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            # TODO: make this more customizable, may not be appropriate for some
            # languages.

            # Make all lowercase, add space between words and punctuation
            line = line.lower()
            line = re.sub(r"([?.!,¿])", r" \1 ", line)
            line = re.sub(r'[" "]+', " ", line)

            lines.append(f'{START_TOKEN} {line.strip()} {END_TOKEN}')
    return '\n'.join(lines)


# class Dataset:
#     """ A model of simple bilingual datasets. """

#     def __init__(
#         self,
#         source,
#         target,
#         max_source_vocab: int = 32000,
#         max_target_vocab: int = 32000,
#         max_sequence_length=40,
#     ) -> None:
#         """ Set up dataset. Raise an InvalidDatasetException if the input and
#             output don't have the same dimension.
        
#         Parameters:
#             source: The input data points, as a list of strings (e.g. a list of
#                     sentences, in the source language).
#             target: The output data points, as a list of strings (e.g. a list of
#                     sentences, in the target language).
#         """
#         if len(source) != len(target):
#             ERROR_MESSAGE = 'Number of source and target points are not equal.'
#             raise InvalidDatasetError(ERROR_MESSAGE)
        

#         self._source = source
#         self._target = target

#         self._datasets = None
#         self._is_shuffled = False
#         self._is_tokenized = False

#         self._max_sequence_length = max_sequence_length
#         self._max_source_vocab = max_source_vocab
#         self._max_target_vocab = max_target_vocab
      
#     def get_max_sequence_length(self):
#       return self._max_sequence_length
    
#     def _get_vocabs(self, vocab_method):
#       reserved_tokens = [PAD_TOKEN, OOV_TOKEN, START_TOKEN, END_TOKEN]

#       if vocab_method == 'bert':
#           # Train word piece for source
#           bert_vocab_args = dict(
#               vocab_size=self._max_source_vocab,
#               reserved_tokens=reserved_tokens,
#               bert_tokenizer_params={"lower_case": True},
#           )

#           source_word_piece_ds = tf.data.Dataset.from_tensor_slices(self._datasets.get('source_train'))
#           source_vocab = bert_vocab.bert_vocab_from_dataset(
#               source_word_piece_ds.batch(1000).prefetch(2), **bert_vocab_args
#           )

#           # Train word piece for target
#           bert_vocab_args = dict(
#               vocab_size=self._max_target_vocab,
#               reserved_tokens=reserved_tokens,
#               bert_tokenizer_params={"lower_case": True},
#           )

#           target_word_piece_ds = tf.data.Dataset.from_tensor_slices(self._datasets.get('target_train'))
#           target_vocab = bert_vocab.bert_vocab_from_dataset(
#               target_word_piece_ds.batch(1000).prefetch(2), **bert_vocab_args
#           )

#           return source_vocab, target_vocab

#     def tokenize(self, tokenizer_type='wordpiece', vocab_method='bert'):
#         """ Creates the tokenizers and trains them on the training data only.

#         Options for tokenizer_type are:
#           - 'wordpiece' --> WordPieceTokenizer
#           - 'bpe' --> BytePairTokenizer
#           - 'unicode' --> UnicodeCharacterTokenizer
        
#         Options for vocab_method:
#           - 'bert': use bert_vocab_from_dataset to learn the vocab (i.e. subwords)
#           - 'spaces': Just split about spaces to get words (no subwords)
        
#         TODO: currently only supports bert not spaces, and only supports tokenizer_type = wordpiece
#         """

#         source_vocab, target_vocab = self._get_vocabs(vocab_method)

#         if tokenizer_type == 'wordpiece':
#             self._source_tokenizer = keras_nlp.tokenizers.WordPieceTokenizer(
#                 vocabulary=source_vocab, lowercase=False, oov_token=OOV_TOKEN
#             )

#             self._target_tokenizer = keras_nlp.tokenizers.WordPieceTokenizer(
#                 vocabulary=target_vocab, lowercase=False, oov_token=OOV_TOKEN
#             )

#         self._tokenized = True

#     def is_shuffled(self) -> bool:
#         """ Returns True iff the dataset has been shuffled. """
#         return self._is_shuffled

#     def shuffle(self):
#         """ Shuffles the dataset. """
#         # TODO: allow user to specify seed?
#         total_data = list(zip(self._source, self._target))
#         shuffle(total_data)
#         self._source, self._target = zip(*total_data)
#         self._is_shuffled = True

#     def partition_datasets(
#         self,
#         train_amount: float = 0.7,
#         validation_amount: float = 0.15,
#         test_amount: float = 0.15
#     ) -> None:
#         """ Partitions dataset into the requested proportions.
        
#             Note: this method DOES NOT randomly partition, but instead takes the
#             first section of the data as training, the next segment as
#             validation, and the final segment as test. In order to randomly
#             partition, shuffle the dataset first using dataset.shuffle.

#             Raises an error if the proportions do not sum to 1.
        
#         Parameters:
#             train_amount: The proportion (in [0, 1]) of data to use for a
#                           training set. Defaults to 0.7 (70%).
#             validation_amount: The proportion (in [0, 1]) of data to use for a
#                                validation set. Defaults to 0.15 (15%).
#             test_amount: The proportion (in [0, 1]) of data to use for a test
#                          set. Defaults to 0.15 (15%).
#         """
#         if train_amount + validation_amount + test_amount != 1:
#             raise InvalidDatasetError('Dataset proportions must sum to 1')

#         total_data_amount = len(self._source)
#         train_idx = int(total_data_amount * train_amount)
#         val_idx = train_idx + int(total_data_amount * validation_amount)

#         self._datasets = {
#             'source_train': list(self._source[:train_idx]),
#             'source_val': list(self._source[train_idx:val_idx]),
#             'source_test': list(self._source[val_idx:]),
#             'target_train': list(self._target[:train_idx]),
#             'target_val': list(self._target[train_idx:val_idx]),
#             'target_test': list(self._target[val_idx:])
#         }

#     def partition_datasets_numerically(
#         self,
#         train_amount: int,
#         validation_amount: int,
#         test_amount: int
#     ) -> None:
#         """ An alternative to the partition_datasets method, which splits the
#             dataset into training, validation and test sets with specified
#             quantities of data, rather than as a proportion of the total
#             dataset.

#             Note: this method DOES NOT randomly partition, but instead takes the
#             first section of the data as training, the next segment as
#             validation, and the final segment as test. In order to randomly
#             partition, shuffle the dataset first using dataset.shuffle.

#             Raises an error if the sum of amounts is greater than the size of
#             the overall dataset.

#             Parameters:
#                 train_amount: #data points to use in the training set.
#                 validation_amount: #data points to use in the validation set.
#                 test_amount: #data points to use in the test set.
#         """
#         if train_amount + validation_amount + test_amount > len(self._source):
#             raise InvalidDatasetError('Amounts must sum to < total data size.')
        
#         train_idx = train_amount
#         val_idx = train_amount + validation_amount
#         test_idx = val_idx + test_amount

#         self._datasets = {
#             'source_train': self._source[:train_idx],
#             'source_val': self._source[train_idx:val_idx],
#             'source_test': self._source[val_idx:test_idx],
#             'target_train': self._target[:train_idx],
#             'target_val': self._target[train_idx:val_idx],
#             'target_test': self._target[val_idx:test_idx]
#         }

#     def get_raw_data(self):
#         """ Returns the raw total dataset, as a tuple of
#             (source sentences, target sentences).
#         """
#         return self._source, self._target
    
#     def get_datasets(self):
#         """ Returns a dictionary of the datasets, if the dataset has been split
#             into sets, else None. The keys of this dictionary are:
#                 - 'source_train'
#                 - 'source_val'
#                 - 'source_test'
#                 - 'target_train'
#                 - 'target_val'
#                 - 'target_test'
#         """
#         return self._datasets
    
#     def is_tokenized(self):
#         return self._is_tokenized

#     def create_tensors_from_sentences(self, sentences, max_length=None, source=True):
#         """ Process the sentences from words to their array of integers representation,
#             according to the provided tokenizer, and pad out the end of the sentence with
#             OOV_TOKENs to make all sentences the same length.
        
#             Parameters:
#                 sentences (list<str>): List of sentences to convert to tensors.
#                 tokenizer (Tokenizer)
        
#             Returns:

#         """
#         tokenizer = self._source_tokenizer if source else self._target_tokenizer
#         tensor = tokenizer.texts_to_sequences(sentences)
#         return tensor

#     def sequences_to_texts(self, sequence, source=True):
#         tokenizer = self._source_tokenizer if source else self._target_tokenizer
#         return tokenizer.detokenize(sequence)
    
#     def texts_to_sequences(self, sequence, source=True):
#         tokenizer = self._source_tokenizer if source else self._target_tokenizer
#         return tokenizer.tokenize(sequence)
    
#     def get_start_idx(self, source=True):
#         tokenizer = self._source_tokenizer if source else self._target_tokenizer
#         return tokenizer.token_to_id(START_TOKEN)

#     def get_source_vocab_size(self) -> Optional[int]:
#         return len(self._source_tokenizer.get_vocabulary())
  
#     def get_target_vocab_size(self) -> Optional[int]:
#         return len(self._target_tokenizer.get_vocabulary())
    
#     def get_training_size(self) -> int:
#         return len(self._datasets['source_train'])
    
#     def get_validation_size(self) -> int:
#         return len(self._datasets['source_val'])

#     def get_test_size(self) -> int:
#         return len(self._datasets['source_test'])
    
#     def get_batch_size(self) -> int:
#         return self._batch_size

#     def batch(self, batch_size: int = 64, drop_remainder: bool = True):
#         """ Shuffles and batches the datasets ready for use in training. This
#             should be the last step before using the data in training (i.e. you
#             should have already split your sets and tokenized the data).
        
#             Parameters:
#                 batch_size: The batch size to use.
#                 drop_remainder: If True, data points that don't fit evenly into
#                                 a batch are dropped. Defaults to True.
            
#             TODO: separate this out into multiple methods so can prepare test separately
#         """
#         buffer_size = self.get_source_vocab_size()
#         self._batch_size = batch_size

#         train_data = (self._datasets['source_train'], self._datasets['target_train'])
#         dataset = self.make_dataset(*train_data, batch_size=batch_size)

#         val_data = (self._datasets['source_val'], self._datasets['target_val'])
#         val_dataset = self.make_dataset(*val_data, batch_size=batch_size)

#         test_data = (self._datasets['source_test'], self._datasets['target_test'])
#         test_dataset = self.make_dataset(*test_data, batch_size=1) # TODO: batch size here??
#         return dataset, val_dataset, test_dataset

#     def preprocess_batch(self, source, target):
#         batch_size = tf.shape(target)[0]

#         source = self._source_tokenizer(source)
#         target = self._target_tokenizer(target)

#         # Pad `eng` to `MAX_SEQUENCE_LENGTH`.
#         source_start_end_packer = keras_nlp.layers.StartEndPacker(
#             sequence_length=MAX_SEQUENCE_LENGTH,
#             pad_value=self._source_tokenizer.token_to_id(PAD_TOKEN),
#         )
#         source = source_start_end_packer(source)

#         # Add special tokens (`"[START]"` and `"[END]"`) to `spa` and pad it as well.
#         target_start_end_packer = keras_nlp.layers.StartEndPacker(
#             sequence_length=MAX_SEQUENCE_LENGTH + 1,
#             start_value=self._target_tokenizer.token_to_id(START_TOKEN),
#             end_value=self._target_tokenizer.token_to_id(END_TOKEN),
#             pad_value=self._target_tokenizer.token_to_id(PAD_TOKEN),
#         )
#         target = target_start_end_packer(target)

#         return (
#             {
#                 "encoder_inputs": source,
#                 "decoder_inputs": target[:, :-1],
#             },
#             target[:, 1:],
#         )

#     def make_dataset(self, source_texts, target_texts, batch_size=64):
#         dataset = tf.data.Dataset.from_tensor_slices((source_texts, target_texts))
#         dataset = dataset.batch(batch_size)
#         dataset = dataset.map(self.preprocess_batch, num_parallel_calls=tf.data.AUTOTUNE)
#         return dataset.shuffle(2048).prefetch(16).cache()




class Dataset:
    """ A model of simple bilingual datasets. Handles processing and tokenization,
        data splitting, and data management.
    """

    def __init__(
        self,
        source: str,
        target: str,
        source_sep: str = '\n',
        target_sep: str = '\n'
    ) -> None:
        """ Set up dataset. Raise an InvalidDatasetException if the input and
            output don't have the same dimension.
        
        Parameters:
            source: The entire source text as one string.
            target: The entire target text as one string.
            source_sep: The separator about which to split the source text.
                        Uses newline character as the default separator.
            target_sep: The separator about which to split the target text.
                        Uses newline character as the default separator.           
        """
        self._source = self._process_raw_data(source, source_sep)
        self._target = self._process_raw_data(target, target_sep)

        if len(self._source) != len(self._target):
            ERROR_MESSAGE = 'Number of source and target points are not equal.'
            raise InvalidDatasetError(ERROR_MESSAGE)
        # self._source = source
        # self._target = target

        self._datasets = None
        self._is_shuffled = False
        self._is_tokenized = False
    
    def _process_raw_data(self, data: str, sep: str) -> list[str]:
        """ Splits up the data string about the separator and does
            some basic pre-processing. """
        return [line for line in data.split(sep)]

    def is_shuffled(self) -> bool:
        """ Returns True iff the dataset has been shuffled. """
        return self._is_shuffled

    def shuffle(self):
        """ Shuffles the dataset. """
        # TODO: allow user to specify seed?
        total_data = list(zip(self._source, self._target))
        shuffle(total_data)
        self._source, self._target = zip(*total_data)
        self._is_shuffled = True

    def partition_datasets(
        self,
        train_amount: float = 0.7,
        validation_amount: float = 0.15,
        test_amount: float = 0.15
    ) -> None:
        """ Partitions dataset into the requested proportions.
        
            Note: this method DOES NOT randomly partition, but instead takes the
            first section of the data as training, the next segment as
            validation, and the final segment as test. In order to randomly
            partition, shuffle the dataset first using dataset.shuffle.

            Raises an error if the proportions do not sum to 1.
        
        Parameters:
            train_amount: The proportion (in [0, 1]) of data to use for a
                          training set. Defaults to 0.7 (70%).
            validation_amount: The proportion (in [0, 1]) of data to use for a
                               validation set. Defaults to 0.15 (15%).
            test_amount: The proportion (in [0, 1]) of data to use for a test
                         set. Defaults to 0.15 (15%).
        """
        if train_amount + validation_amount + test_amount != 1:
            raise InvalidDatasetError('Dataset proportions must sum to 1')

        total_data_amount = len(self._source)
        train_idx = int(total_data_amount * train_amount)
        val_idx = train_idx + int(total_data_amount * validation_amount)

        self._datasets = {
            'source_train': self._source[:train_idx],
            'source_val': self._source[train_idx:val_idx],
            'source_test': self._source[val_idx:],
            'target_train': self._target[:train_idx],
            'target_val': self._target[train_idx:val_idx],
            'target_test': self._target[val_idx:]
        }

    def get_raw_data(self) -> tuple[list[str], list[str]]:
        """ Returns the raw total dataset, as a tuple of
            (source sentences, target sentences).
        """
        return self._source, self._target
    
    def get_datasets(self, tokenized=False) -> Optional[dict[str, list[str]]]:
        """ Returns a dictionary of the datasets, if the dataset has been split
            into sets, else None. The keys of this dictionary are:
                - 'source_train'
                - 'source_val'
                - 'source_test'
                - 'target_train'
                - 'target_val'
                - 'target_test'
        """
        if tokenized:
            return self._tokenized_datasets
        return self._datasets

    def create_tensors_from_sentences(self, sentences, max_length=None, source=True):
        """ Process the sentences from words to their array of integers representation,
            according to the provided tokenizer, and pad out the end of the sentence with
            OOV_TOKENs to make all sentences the same length.
        
            Parameters:
                sentences (list<str>): List of sentences to convert to tensors.
                tokenizer (Tokenizer)
        
            Returns:

        """
        tokenizer = self._source_tokenizer if source else self._target_tokenizer
        tensor = tokenizer.texts_to_sequences(sentences)
        if max_length is not None:
            tensor = pad_sequences(tensor, maxlen=max_length, padding='post')
        else:
            tensor = pad_sequences(tensor, padding='post')
        
        return tensor

    def tokenize(
        self,
        tokenizer_type: str = 'WordPiece',
        make_lowercase: bool = True,
        max_source_length: int = 25,
        max_target_length: int = 25,
        max_source_vocab_size: int = 1000,
        max_target_vocab_size: int = 1000,
    ):
        """ Create tokenizer and tensor of sequences for the iterable of sentences
            from a particular language.

            NOTE: this is just a simple keras tokenizer, and should be replaced
            later with something more sophisticated, like sentencepiece.

            Parameters:
                lang (iter<str>): Sentences from a particular language.

            Returns:
                (tuple<np.array, Tokenizer>): The tensor of sequences (shape:
                                            (#samples, #timesteps)), and the
                                            Tokenizer for this language.
        """
        self._max_source_length = max_source_length
        self._max_target_length = max_target_length

        # Create vocabs & tokenizers and fit to training data
        if tokenizer_type == 'WordPiece':
            source_vocab = keras_nlp.tokenizers.compute_word_piece_vocabulary(
                tf.data.Dataset.from_tensor_slices(list(self._datasets['source_train'])),
                vocabulary_size=max_source_vocab_size,
                reserved_tokens=[START_TOKEN, END_TOKEN, OOV_TOKEN, PAD_TOKEN],
                lowercase=make_lowercase,
            )
            self._source_tokenizer = keras_nlp.tokenizers.WordPieceTokenizer(
                vocabulary=source_vocab,
                sequence_length=self._max_source_length,
                lowercase=make_lowercase,
                oov_token=OOV_TOKEN
            )

            target_vocab = keras_nlp.tokenizers.compute_word_piece_vocabulary(
                tf.data.Dataset.from_tensor_slices(list(self._datasets['target_train'])),
                max_target_vocab_size,
                reserved_tokens=[START_TOKEN, END_TOKEN, OOV_TOKEN, PAD_TOKEN],
                lowercase=make_lowercase,
            )
            self._target_tokenizer = keras_nlp.tokenizers.WordPieceTokenizer(
                vocabulary=target_vocab,
                sequence_length=self._max_target_length,
                lowercase=make_lowercase,
                oov_token=OOV_TOKEN
            )

        # Tokenize datasets with trained tokenizers
        source_tokenizer = self._source_tokenizer
        target_tokenizer = self._target_tokenizer
        self._tokenized_datasets = {
            'source_train': source_tokenizer(self._datasets['source_train']),
            'source_val': source_tokenizer(self._datasets['source_val']),
            'source_test': source_tokenizer(self._datasets['source_test']),
            'target_train': target_tokenizer(self._datasets['target_train']),
            'target_val': target_tokenizer(self._datasets['target_val']),
            'target_test': target_tokenizer(self._datasets['target_test'])
        }

        self._is_tokenized = True

    def is_tokenized(self) -> bool:
        return self._is_tokenized
    
    def get_source_vocab_size(self):
        return self._source_tokenizer.vocabulary_size()
    
    def tokenize_text(self, sentences, source=True):
        tokenizer = self._source_tokenizer if source else self._target_tokenizer
        return tokenizer(sentences)

    def get_tokenizers(self):
        return self._source_tokenizer, self._target_tokenizer

    def get_target_vocab_size(self):
        return self._target_tokenizer.vocabulary_size()

    def get_training_size(self) -> int:
        return len(self._datasets['source_train'])
    
    def get_validation_size(self) -> int:
        return len(self._datasets['source_val'])

    def get_test_size(self) -> int:
        return len(self._datasets['source_test'])
    
    def get_batch_size(self) -> int:
        return self._batch_size

    def preprocess_batch(self, source, target):
        """ TODO: this structure assumes that we're pre-processing for a transformer. Maybe
            makes more sense to have as a model function """
        # batch_size = tf.shape(spa)[0]
        batch_size = self._batch_size

        source = self._source_tokenizer(source)
        target = self._target_tokenizer(target)

        # Pad `eng` to `MAX_SEQUENCE_LENGTH`.
        source_start_end_packer = keras_nlp.layers.StartEndPacker(
            sequence_length=self._max_source_length,
            pad_value=self._source_tokenizer.token_to_id(PAD_TOKEN),
        )
        source = source_start_end_packer(source)

        # Add special tokens (`"[START]"` and `"[END]"`) to `spa` and pad it as well.
        target_start_end_packer = keras_nlp.layers.StartEndPacker(
            sequence_length=self._max_target_length + 1,
            start_value=self._target_tokenizer.token_to_id(START_TOKEN),
            end_value=self._target_tokenizer.token_to_id(END_TOKEN),
            pad_value=self._target_tokenizer.token_to_id(PAD_TOKEN),
        )
        target = target_start_end_packer(target)

        return (
            {
                "encoder_inputs": source,
                "decoder_inputs": target[:, :-1],
            },
            target[:, 1:],
        )

    def make_dataset(self, source: list[str], target: list[str]):
        dataset = tf.data.Dataset.from_tensor_slices((list(source), list(target)))
        dataset = dataset.batch(self._batch_size)
        dataset = dataset.map(self.preprocess_batch, num_parallel_calls=tf.data.AUTOTUNE)
        return dataset.shuffle(2048).prefetch(16).cache()

    def batch(self, batch_size: int = 64, drop_remainder: bool = True) -> tuple[tf.data.Dataset]:
        """ Shuffles and batches the datasets ready for use in training. This
            should be the last step before using the data in training (i.e. you
            should have already split your sets and tokenized the data).
        
            Parameters:
                batch_size: The batch size to use.
                drop_remainder: If True, data points that don't fit evenly into
                                a batch are dropped. Defaults to True.
            
            TODO: separate this out into multiple methods so can prepare test separately
        """
        buffer_size = self.get_source_vocab_size()
        self._batch_size = batch_size

        train_data = (self._datasets['source_train'], self._datasets['target_train'])
        dataset = self.make_dataset(*train_data)
        # dataset = tf.data.Dataset.from_tensor_slices(train_data)
        # dataset = dataset.shuffle(buffer_size)
        # dataset = dataset.batch(batch_size, drop_remainder=drop_remainder)

        val_data = (self._datasets['source_val'], self._datasets['target_val'])
        val_dataset = self.make_dataset(*val_data)
        # val_dataset = tf.data.Dataset.from_tensor_slices(val_data)
        # val_dataset = val_dataset.shuffle(buffer_size)
        # val_dataset = val_dataset.batch(batch_size, drop_remainder=True)

        test_data = (self._datasets['source_test'], self._datasets['target_test'])
        test_dataset = self.make_dataset(*test_data)
        # test_dataset = tf.data.Dataset.from_tensor_slices(test_data)
        # test_dataset = test_dataset.shuffle(self.get_test_size())

        return dataset, val_dataset, test_dataset

# class Dataset:
#     """ A model of simple bilingual datasets. """

#     def __init__(self, source: list[str], target: list[str]) -> None:
#         """ Set up dataset. Raise an InvalidDatasetException if the input and
#             output don't have the same dimension.
        
#         Parameters:
#             source: The input data points, as a list of strings (e.g. a list of
#                     sentences, in the source language).
#             target: The output data points, as a list of strings (e.g. a list of
#                     sentences, in the target language).
#         """
#         if len(source) != len(target):
#             ERROR_MESSAGE = 'Number of source and target points are not equal.'
#             raise InvalidDatasetError(ERROR_MESSAGE)
#         self._source = source
#         self._target = target

#         self._datasets = None
#         self._is_shuffled = False
#         self._is_tokenized = False
    
#     def is_shuffled(self) -> bool:
#         """ Returns True iff the dataset has been shuffled. """
#         return self._is_shuffled

#     def shuffle(self):
#         """ Shuffles the dataset. """
#         # TODO: allow user to specify seed?
#         total_data = list(zip(self._source, self._target))
#         shuffle(total_data)
#         self._source, self._target = zip(*total_data)
#         self._is_shuffled = True

#     def partition_datasets(
#         self,
#         train_amount: float = 0.7,
#         validation_amount: float = 0.15,
#         test_amount: float = 0.15
#     ) -> None:
#         """ Partitions dataset into the requested proportions.
        
#             Note: this method DOES NOT randomly partition, but instead takes the
#             first section of the data as training, the next segment as
#             validation, and the final segment as test. In order to randomly
#             partition, shuffle the dataset first using dataset.shuffle.

#             Raises an error if the proportions do not sum to 1.
        
#         Parameters:
#             train_amount: The proportion (in [0, 1]) of data to use for a
#                           training set. Defaults to 0.7 (70%).
#             validation_amount: The proportion (in [0, 1]) of data to use for a
#                                validation set. Defaults to 0.15 (15%).
#             test_amount: The proportion (in [0, 1]) of data to use for a test
#                          set. Defaults to 0.15 (15%).
#         """
#         if train_amount + validation_amount + test_amount != 1:
#             raise InvalidDatasetError('Dataset proportions must sum to 1')

#         total_data_amount = len(self._source)
#         train_idx = int(total_data_amount * train_amount)
#         val_idx = train_idx + int(total_data_amount * validation_amount)

#         self._datasets = {
#             'source_train': self._source[:train_idx],
#             'source_val': self._source[train_idx:val_idx],
#             'source_test': self._source[val_idx:],
#             'target_train': self._target[:train_idx],
#             'target_val': self._target[train_idx:val_idx],
#             'target_test': self._target[val_idx:]
#         }

#     def partition_datasets_numerically(
#         self,
#         train_amount: int,
#         validation_amount: int,
#         test_amount: int
#     ) -> None:
#         """ An alternative to the partition_datasets method, which splits the
#             dataset into training, validation and test sets with specified
#             quantities of data, rather than as a proportion of the total
#             dataset.

#             Note: this method DOES NOT randomly partition, but instead takes the
#             first section of the data as training, the next segment as
#             validation, and the final segment as test. In order to randomly
#             partition, shuffle the dataset first using dataset.shuffle.

#             Raises an error if the sum of amounts is greater than the size of
#             the overall dataset.

#             Parameters:
#                 train_amount: #data points to use in the training set.
#                 validation_amount: #data points to use in the validation set.
#                 test_amount: #data points to use in the test set.
#         """
#         if train_amount + validation_amount + test_amount > len(self._source):
#             raise InvalidDatasetError('Amounts must sum to < total data size.')
        
#         train_idx = train_amount
#         val_idx = train_amount + validation_amount
#         test_idx = val_idx + test_amount

#         self._datasets = {
#             'source_train': self._source[:train_idx],
#             'source_val': self._source[train_idx:val_idx],
#             'source_test': self._source[val_idx:test_idx],
#             'target_train': self._target[:train_idx],
#             'target_val': self._target[train_idx:val_idx],
#             'target_test': self._target[val_idx:test_idx]
#         }

#     def get_raw_data(self) -> tuple[list[str], list[str]]:
#         """ Returns the raw total dataset, as a tuple of
#             (source sentences, target sentences).
#         """
#         return self._source, self._target
    
#     def get_datasets(self) -> Optional[dict[str, list[str]]]:
#         """ Returns a dictionary of the datasets, if the dataset has been split
#             into sets, else None. The keys of this dictionary are:
#                 - 'source_train'
#                 - 'source_val'
#                 - 'source_test'
#                 - 'target_train'
#                 - 'target_val'
#                 - 'target_test'
#         """
#         return self._datasets
    
#     def is_tokenized(self):
#         return self._is_tokenized

#     def create_tensors_from_sentences(self, sentences, max_length=None, source=True):
#         """ Process the sentences from words to their array of integers representation,
#             according to the provided tokenizer, and pad out the end of the sentence with
#             OOV_TOKENs to make all sentences the same length.
        
#             Parameters:
#                 sentences (list<str>): List of sentences to convert to tensors.
#                 tokenizer (Tokenizer)
        
#             Returns:

#         """
#         tokenizer = self._source_tokenizer if source else self._target_tokenizer
#         tensor = tokenizer.texts_to_sequences(sentences)
#         if max_length is not None:
#             tensor = pad_sequences(tensor, maxlen=max_length, padding='post')
#         else:
#             tensor = pad_sequences(tensor, padding='post')
        
#         return tensor

#     def tokenize(self):
#         """ Create tokenizer and tensor of sequences for the iterable of sentences
#             from a particular language.

#             NOTE: this is just a simple keras tokenizer, and should be replaced
#             later with something more sophisticated, like sentencepiece.

#             Parameters:
#                 lang (iter<str>): Sentences from a particular language.

#             Returns:
#                 (tuple<np.array, Tokenizer>): The tensor of sequences (shape:
#                                             (#samples, #timesteps)), and the
#                                             Tokenizer for this language.
#         """
#         # Create tokenizers and fit to training data
#         self._source_tokenizer = Tokenizer(filters='', oov_token=OOV_TOKEN)
#         self._source_tokenizer.fit_on_texts(self._datasets['source_train'])

#         self._target_tokenizer = Tokenizer(filters='', oov_token=OOV_TOKEN)
#         self._target_tokenizer.fit_on_texts(self._datasets['target_train'])

#         # Tokenize datasets with trained tokenizers
#         source = self.create_tensors_from_sentences(self._datasets['source_train'])
#         self._max_source_length = source.shape[1]

#         target = self.create_tensors_from_sentences(self._datasets['target_train'], source=False)
#         self._max_target_length = target.shape[1]

#         source_val = self.create_tensors_from_sentences(self._datasets['source_val'], max_length=self._max_source_length)
#         target_val = self.create_tensors_from_sentences(self._datasets['target_val'], max_length=self._max_target_length, source=False)

#         source_test = self.create_tensors_from_sentences(self._datasets['source_test'], max_length=self._max_source_length)
#         target_test = self.create_tensors_from_sentences(self._datasets['target_test'], max_length=self._max_target_length, source=False)

#         self._datasets = {
#             'source_train': source,
#             'source_val': source_val,
#             'source_test': source_test,
#             'target_train': target,
#             'target_val': target_val,
#             'target_test': target_test
#         }

#         self._is_tokenized = True

#     def sequences_to_texts(self, sequence, source=True):
#         tokenizer = self._source_tokenizer if source else self._target_tokenizer
#         return tokenizer.sequences_to_texts(sequence)
    
#     def texts_to_sequences(self, sequence, source=True):
#         tokenizer = self._source_tokenizer if source else self._target_tokenizer
#         return tokenizer.texts_to_sequences(sequence)
    
#     def get_start_idx(self, source=True):
#         tokenizer = self._source_tokenizer if source else self._target_tokenizer
#         return tokenizer.word_index[START_TOKEN]
    
#     def idx_to_word(self, idx: int, source=True):
#         tokenizer = self._source_tokenizer if source else self._target_tokenizer
#         if idx >= len(tokenizer.index_word):
#             return OOV_TOKEN
#         return tokenizer.index_word[idx]

#     # def tokenize(self, model_type: str = 'unigram', max_vocab_size: int = 32000, source_model: str = None, target_model: str = None):
#     #     """ Tokenizes datasets using the specified subword segmentation
#     #         algorithm.

#     #         Trains the subword segmentation algorithm on the training set only.

#     #         Parameters:
#     #             model_type: Algorithm to use for subword segmentation. Options
#     #                         are 'unigram', 'bpe', 'char', or 'word'. See
#     #                         https://github.com/google/sentencepiece for more
#     #                         information.
#     #             max_vocab_size: Maximum number of tokens in each vocabulary. The
#     #                             resulting vocabularies may have a size smaller
#     #                             than this amount, but not larger.
#     #             source_model: If not None, this will be used instead of training
#     #                           a new source model.
#     #             target_model: If not None, this will be used instead of training
#     #                           a new target model.
#     #     """

#     #     # Save training sets into temporary files to be used in training the
#     #     # subword segmenter
#     #     source_train = self._datasets['source_train']
#     #     target_train = self._datasets['target_train']

#     #     from tempfile import NamedTemporaryFile
#     #     train_source_file = NamedTemporaryFile().name
#     #     train_target_file = NamedTemporaryFile().name

#     #     np.savetxt(train_source_file, source_train, fmt='%s')
#     #     np.savetxt(train_target_file, target_train, fmt='%s')

#     #     if source_model is None:
#     #         spm.SentencePieceTrainer.Train(f'--input={train_source_file} --model_prefix=src_sp --vocab_size={max_vocab_size} --model_type={model_type} --hard_vocab_limit=False')
#     #         source_model = './src_sp.model'
#     #     # Train spm models
        
#     #     self._sp_source = spm.SentencePieceProcessor()
#     #     self._sp_source.load(source_model)

#     #     if target_model is None:
#     #         spm.SentencePieceTrainer.Train(f'--input={train_target_file} --model_prefix=trg_sp --vocab_size={max_vocab_size} --model_type={model_type} --hard_vocab_limit=False')
#     #         target_model = './trg_sp.model'

#     #     self._sp_target = spm.SentencePieceProcessor()
#     #     self._sp_target.load(source_model)

#     #     # Tokenize each dataset with the sentence piece model
#     #     source = self.tokenize_with_sp(source_train)
#     #     source = pad_sequences(source, padding='post')

#     #     target = self.tokenize_with_sp(target_train, source=False)
#     #     target = pad_sequences(target, padding='post')

#     #     source_vocab_size = len(source[0])
#     #     target_vocab_size = len(target[0])

#     #     source_val = self.tokenize_with_sp(self._datasets['source_val'])
#     #     source_val = pad_sequences(source_val, maxlen=source_vocab_size, padding='post')

#     #     target_val = self.tokenize_with_sp(self._datasets['target_val'], source=False)
#     #     target_val = pad_sequences(target_val, maxlen=target_vocab_size, padding='post')

#     #     source_test = self.tokenize_with_sp(self._datasets['source_test'])
#     #     source_test = pad_sequences(source_test, maxlen=source_vocab_size, padding='post')

#     #     target_test = self.tokenize_with_sp(self._datasets['target_test'], source=False)
#     #     target_test = pad_sequences(target_test, maxlen=target_vocab_size, padding='post')

#     #     self._datasets = {
#     #         'source_train': source,
#     #         'source_val': source_val,
#     #         'source_test': source_test,
#     #         'target_train': target,
#     #         'target_val': target_val,
#     #         'target_test': target_test
#     #     }

#     #     self._is_tokenized = True

#     def _shrink(self, train_size, val_size, test_size):
#         self._datasets['source_train'] = self._datasets['source_train'][:train_size]
#         self._datasets['target_train'] = self._datasets['target_train'][:train_size]

#         self._datasets['source_val'] = self._datasets['source_val'][:val_size]
#         self._datasets['target_val'] = self._datasets['target_val'][:val_size]

#         self._datasets['source_test'] = self._datasets['source_test'][:test_size]
#         self._datasets['target_test'] = self._datasets['target_test'][:test_size]

#     # def tokenize_with_sp(self, sentences, source=True):
#     #     sp = self._sp_source if source else self._sp_target
#     #     return [sp.EncodeAsIds(sentence) for sentence in sentences]

#     # def indices_to_language(self, indices, source=True):
#     #     sp = self._sp_source if source else self._sp_target
#     #     return sp.DecodeIds(indices[0].tolist())
#     #     # return ' '.join([word for word in sp.DecodeIds(indices) if word != START_TOKEN and word != END_TOKEN])

#     # def id_to_piece(self, _id, source=True):
#     #     sp = self._sp_source if source else self._sp_target
#     #     # TODO: i don't know that this should need this
#     #     try:
#     #         return sp.IdToPiece(_id)
#     #     except IndexError:
#     #         return 'UNK'
    
#     # def piece_to_id(self, piece, source=True):
#     #     sp = self._sp_source if source else self._sp_target
#     #     return sp.PieceToId(piece)

#     # def decode_pieces(self, pieces, source=True):
#     #     sp = self._sp_source if source else self._sp_target
#     #     return sp.DecodePieces(pieces)

#     def get_source_vocab_size(self) -> Optional[int]:
#         if self._is_tokenized:
#             return self._datasets['source_train'].shape[1]

#     def get_target_vocab_size(self) -> Optional[int]:
#         if self._is_tokenized:
#             return self._datasets['target_train'].shape[1]
    
#     def get_training_size(self) -> int:
#         return len(self._datasets['source_train'])
    
#     def get_validation_size(self) -> int:
#         return len(self._datasets['source_val'])

#     def get_test_size(self) -> int:
#         return len(self._datasets['source_test'])
    
#     def get_batch_size(self) -> int:
#         return self._batch_size

#     def batch(self, batch_size: int = 64, drop_remainder: bool = True) -> tuple[tf.data.Dataset]:
#         """ Shuffles and batches the datasets ready for use in training. This
#             should be the last step before using the data in training (i.e. you
#             should have already split your sets and tokenized the data).
        
#             Parameters:
#                 batch_size: The batch size to use.
#                 drop_remainder: If True, data points that don't fit evenly into
#                                 a batch are dropped. Defaults to True.
            
#             TODO: separate this out into multiple methods so can prepare test separately
#         """
#         buffer_size = self.get_source_vocab_size()
#         self._batch_size = batch_size

#         train_data = (self._datasets['source_train'], self._datasets['target_train'])
#         dataset = tf.data.Dataset.from_tensor_slices(train_data)
#         dataset = dataset.shuffle(buffer_size)
#         dataset = dataset.batch(batch_size, drop_remainder=drop_remainder)

#         val_data = (self._datasets['source_val'], self._datasets['target_val'])
#         val_dataset = tf.data.Dataset.from_tensor_slices(val_data)
#         val_dataset = val_dataset.shuffle(buffer_size)
#         val_dataset = val_dataset.batch(batch_size, drop_remainder=True)

#         test_data = (self._datasets['source_test'], self._datasets['target_test'])
#         test_dataset = tf.data.Dataset.from_tensor_slices(test_data)
#         test_dataset = test_dataset.shuffle(self.get_test_size())

#         return dataset, val_dataset, test_dataset