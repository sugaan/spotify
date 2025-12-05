"""Unit tests with mock."""
import pytest
import pandas as pd
from unittest.mock import patch
from src.loader import load_spotify_data

def test_load_spotify_data():
    """Test loader with mocked DF and engine."""
    test_df = pd.DataFrame({"track": ["test"]})
    
    with patch('src.loader.pd.read_csv') as mock_csv, \
         patch('src.loader.create_engine') as mock_engine:
        mock_csv.return_value = test_df
        mock_engine.return_value.__enter__.return_value = None
        
        result = load_spotify_data('fake.csv')
        assert "loaded 1 rows" in result
        mock_csv.assert_called_once()