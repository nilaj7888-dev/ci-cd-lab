from calc import add

def test_add():
    assert add(2, 3) == 5
    
print("✅ All tests passed!")
test_add()
```

4. Commit with message: `Add test_calc.py`

### **Step 3: The Workflow Will Automatically Run Again!**

After you commit these files, GitHub Actions will automatically trigger again, and this time it will work! ✅

---

## 📁 Your Repository Should Have These Files:
```
ci-cd-lab/
├── .github/
│   └── workflows/
│       └── hello-ci.yml  ✅ You have this
├── calc.py              ❌ MISSING - Create this!
├── test_calc.py         ❌ MISSING - Create this!
└── README.md
